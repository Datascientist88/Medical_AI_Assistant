# Conversational AI Doctor Assistant  
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)](https://streamlit.io/)  
[![LangChain](https://img.shields.io/badge/Built%20with-LangChain-blue)](https://www.langchain.com/)  
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)  
[![Developed by](https://img.shields.io/badge/Developed%20By-Mohammed%20Bahageel-orange)](https://github.com/Datascientist88)

---

![Doctor AI Assistant](assets/AI.gif)

## 🚀 About the Project

The **Conversational AI Doctor Assistant** is a Python-based application that leverages **Streamlit** and **LangChain** to provide medical guidance and support through natural language conversations. Powered by **Retrieval-Augmented Generation (RAG)**, this assistant provides accurate and context-aware answers by retrieving relevant data from medical sources and augmenting it with generative AI capabilities.

This assistant aims to serve as a reliable tool for preliminary medical consultations, making healthcare guidance more accessible.

---

## 🏗️ Built With

### 🔧 Frameworks and Tools
- **Streamlit**: For building an interactive and user-friendly web interface.
- **LangChain**: For managing conversational AI flows and retrieval-augmented generation.
- **Python**: The primary language for developing the app's backend and AI components.

### 📚 Key Features
1. **Natural Language Understanding**: Engages in realistic conversations about medical queries.
2. **RAG Integration**: Combines document retrieval with generative AI for precise and contextually accurate answers.
3. **Interactive Interface**: Built with Streamlit for seamless user interactions.
4. **Expandable Knowledge Base**: Allows easy integration of additional medical knowledge sources.
5. **Text and Audio Input**: Supports both text and voice interactions.

---

## 🌟 Features

- **Real-Time Medical Consultation**: Users can ask health-related questions and receive instant responses.
- **Speech-to-Text Support**: Converts audio queries into text for processing.
- **Customizable Backend**: Easily configure the RAG pipeline with new datasets.
- **User-Friendly Interface**: Designed to be accessible for both medical professionals and non-specialists.

---

## 💡 How It Works

1. **Input**: Users provide their query via text or audio.
2. **Retrieval**: Relevant medical documents are fetched from a pre-indexed knowledge base.
3. **Generation**: AI models augment the retrieved data to generate a detailed and contextual response.
4. **Output**: The response is displayed on the Streamlit interface and can also be played back as audio.

---

## 🛠️ Installation and Setup

### Prerequisites
- Python 3.8 or later
- Pip

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/MohammedBahageel/doctor-ai-assistant.git
   cd doctor-ai-assistant
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

4. **Access the App**  
   Open your browser and navigate to `http://localhost:8501`.

---

## 📂 Project Structure

```plaintext
.
├── app.py                  # Main Streamlit application
├── templates                # prompt templates
|    └──prompt.py         
├──utils/                    # Backend logic for RAG pipeline
│   └── functions.py         # Retrieval module
│                            # Utility functions
├── assets/                  # Static assets (images, etc.)
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── LICENSE                  # License file
```

---

## 🌐 Demo

A live demo of the **Conversational AI Doctor Assistant** is available [here](#).  


---

## 🧑‍💻 About the Developer

This project was developed by **Mohammed Bahageel**, an Artificial Intelligence Developer passionate about creating intelligent and accessible AI solutions for real-world problems.

- GitHub: [MohammedBahageel](https://github.com/Datascientist88)  
- LinkedIn: [Mohammed Bahageel](https://www.linkedin.com/in/mohammed-bahageel-94609b205/)  

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to contribute to this project! Your feedback and suggestions are highly appreciated. 😊



