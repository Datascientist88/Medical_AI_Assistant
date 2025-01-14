import os
import streamlit as st
from streamlit_extras.bottom_container import bottom
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from openai import OpenAI
from templates.carousel import carousel_html
from templates.character import character_3d_component
from utils.functions import (
    get_vector_store,
    get_response,
    text_to_audio,
    autoplay_audio,
    speech_to_text,
)
from streamlit_chat_widget import chat_input_widget
# Initialize OpenAI Client
load_dotenv()
client = OpenAI()

def main():
    # Load and apply custom CSS
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Sidebar content
    with st.sidebar:
        title = "Medical AI Assistant"
        name = "Mohammed Bahageel"
        profession = "Artificial Intelligence Developer"
        imgUrl = "https://cdn.dribbble.com/users/1373613/screenshots/5384701/____-10m.gif"
        st.markdown(
            f"""
            <img class="profileImage" src="{imgUrl}" alt="Your Photo">
            <div class="textContainer">
            <div class="title"><p>{title}</p></div>
            <p>{name}</p>
            <p>{profession}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Embed the clock widget
        # Embed carousel HTML into Streamlit sidebar
        st.components.v1.html(carousel_html, height=250,width=350)
        st.components.v1.html(character_3d_component,height=400,width=300)
    # Initialize session states
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(
                content=" Hello! I'm Medical Assistant . How can I assist you today with your medical inquiries? 🥰"
            )
        ]

    if "vector_store" not in st.session_state:
        st.session_state.vector_store = get_vector_store()

    # Display chat history
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI", avatar="🤖"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human", avatar="👩‍⚕️"):
                st.write(message.content)

    with bottom():
      response = chat_input_widget()
    
    
    user_query = None

    if response:
        if "text" in response:
            user_query = response["text"]
        elif "audioFile" in response:
            with st.spinner("Transcribing audio..."):
                audio_file_bytes = response["audioFile"]
                temp_audio_path = "temp_audio.wav"
                with open(temp_audio_path, "wb") as f:
                    f.write(bytes(audio_file_bytes))
                user_query = speech_to_text(temp_audio_path)
                os.remove(temp_audio_path)

    # Process user input and generate response
    if user_query:
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        with st.chat_message("Human", avatar="👩‍⚕️"):
            st.markdown(user_query)
       # Get AI response
        with st.chat_message("AI", avatar="🤖"):
            response = st.write_stream(get_response(user_query))
            #response_audio_file = "audio_response.mp3"
            #text_to_audio(client, response, response_audio_file)
            #st.audio(response_audio_file)
            #os.remove(response_audio_file)
            st.session_state.chat_history.append(AIMessage(content=response))


if __name__ == "__main__":
   main()