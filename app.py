import os
from dotenv import load_dotenv
import streamlit as st
from streamlit_chat_widget import chat_input_widget
from langchain_core.messages import AIMessage, HumanMessage
from openai import OpenAI
from streamlit_float import *
from utils.functions import (
    get_vector_store,
    get_context_retriever_chain,
    get_conversational_rag_chain,
    get_response,
    text_to_audio,
    autoplay_audio,
    speech_to_text,
)

# load the variables
load_dotenv()
client = OpenAI()

# app layout
def main():
    # Read HTML file
    st.set_page_config("Vitrual Training Assistant", "👩‍⚕️")
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    title = "IVF Virtual Training Assistant "
    name = "Fellowship Program"
    profession = "Doctor Samir Abbas Hospital"
    imgUrl = "https://static.wixstatic.com/media/bee5a4_b73ad21116a347e79fd2c7a9f5879d56~mv2.gif"
    st.markdown(
        f"""
        <div class="st-emotion-cache-18ni7ap ezrtsby2">
                <img class="profileImage" src="{imgUrl}" alt="Your Photo">
            </a>
            <div class="textContainer">
                <div class="title"><p>{title}</p></div>
                <p>{name}</p>
                <p>{profession}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

   

   # Initialize session states
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(
                content=" Hello! I'm Doctor AI Assistant at Doctor Samir Abbas Hospital. How can I assist you today with your medical inquiries? 🥰"
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

    float_init()
    footer_container = st.container()
    with footer_container:
        response = chat_input_widget()
    footer_container.float(
        "display:flex; align-items:center;justify-content:center; overflow:hidden visible;flex-direction:column; position:fixed;bottom:15px;"
    )
    
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
            response_audio_file = "audio_response.mp3"
            text_to_audio(client, response, response_audio_file)
            autoplay_audio(response_audio_file)
            os.remove(response_audio_file)
            st.session_state.chat_history.append(AIMessage(content=response))


if __name__ == "__main__":
    main()