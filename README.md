# Enhanced Q&A Chatbot with Groq 🤖💬

This project is an **interactive Q&A chatbot** built using **Streamlit**, **LangChain**, and **Groq-hosted LLMs**.  
It allows users to ask questions and receive AI-generated answers with **configurable model selection and response parameters**.

The application demonstrates a **clean LangChain pipeline** using prompt templates, output parsers, and Groq models.

---

## 🎯 Objective

The goal of this project is to:
- Build a configurable **Q&A chatbot**
- Demonstrate **LangChain prompt → LLM → parser pipelines**
- Integrate **Groq LLMs** with a simple UI
- Allow users to experiment with different models and generation settings

---

## 🚀 Key Features

### 🤖 Groq-Powered LLMs
- Supports multiple Groq models:
  - `llama-3.1-8b-instant`
  - `llama-3.3-70b-versatile`
  - `openai/gpt-oss-20b`
  - `llama3-groq-8b-tool-use-preview`
- Fast inference with high-quality responses

---

### 🧠 LangChain Prompt Pipeline
- Uses `ChatPromptTemplate` for structured prompts
- Uses `StrOutputParser` for clean text output
- Simple and extensible chain design

---

### 🎛️ Configurable Generation Settings
- Temperature control
- Max token limit control
- Model selection from sidebar

---

### 🖥️ Streamlit-Based UI
- Clean question–answer interface
- Sidebar-based configuration panel
- Secure API key input
- Real-time response generation

---

## 🧠 How It Works

1. User enters a question in the UI
2. Prompt template formats the query
3. The selected Groq LLM generates a response
4. Output parser extracts clean text
5. Answer is displayed to the user

The system follows a **Prompt → LLM → Output Parser** pipeline.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Groq API**
- **LLaMA / OpenAI-compatible models**
- **dotenv**

