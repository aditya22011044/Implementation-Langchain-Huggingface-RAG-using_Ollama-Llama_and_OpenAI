import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")


os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["OPENAI_API_KEY"] = openai_api_key

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])

llm = AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=openai_api_key,
    api_version=api_version,
    deployment_name=deployment_name
)


output_parser=StrOutputParser()

chain=prompt|llm|output_parser

#Streamlit application

st.title('Langchain Demo With OpenAI')
input_text=st.text_input("Search the topic u want")

if input_text:
    st.write(chain.invoke({"question":input_text}))