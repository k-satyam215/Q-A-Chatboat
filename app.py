import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot With GROQ"


## Prompot Template
prompt=ChatPromptTemplate.from_messages(
    [
        ('system','You are a helpful assistant. Please response to the user queries'),
        ('user','Question:{question}')
    ]
)

def generate_response(question, groq_api_key, model_name, temperature, max_tokens):
    if not groq_api_key:
        return "⚠️ Please enter your Groq API key in the sidebar."

    llm = ChatGroq(
        model=model_name,
        groq_api_key=groq_api_key,
        temperature=temperature,
        max_tokens=max_tokens
    )

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

## Title of the app
st.title('Enhanced Q&A Chatbot With Groq')
## Sidebar for settings
st.sidebar.title('Settings')
groq_api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

## Drop down to select various Open AI models
model_name = st.sidebar.selectbox(
    "Select a Groq Model",
    ["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "openai/gpt-oss-20b", "llama3-groq-8b-tool-use-preview"]
)

## Adjust response parameter
temperature=st.sidebar.slider('Temperature',min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider('Max Token',min_value=50,max_value=10000,value=150)

## Main interface for user input
st.write('Go ahead and ask any question')
user_input=st.text_input('You:')

if user_input:
    response=generate_response(user_input,groq_api_key,model_name,temperature,max_tokens)
    st.write(response)
else:
    st.write('Please provide the query')