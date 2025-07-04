# Implementation_Langchain-Huggingface-RAG-using_Ollama-Llama_and_OpenAI


Overview

This project integrates Hugging Face and OpenAI models with LangChain to create a versatile chatbot for natural language processing tasks. It supports both local model execution and cloud-based API calls, with optional GPU acceleration for improved performance.
Features
Leverages Hugging Face models (e.g., Mistral-7B-Instruct-v0.3, GPT-2) for text generation.
Integrates OpenAI's GPT-4o-mini via Azure OpenAI API for advanced language capabilities.
Uses LangChain for prompt engineering and chaining language model tasks.
Supports local and serverless inference with Hugging Face's API.
Configurable via environment variables for secure API key management.


Requirements

Python 3.13.2 or higher
Dependencies listed in requirements.txt:
LangChain and extensions (langchain, langchain-huggingface, langchain_openai, langchain_community, langchain_core)
Hugging Face libraries (huggingface_hub, transformers, accelerate, bitsandbytes)
Streamlit, FastAPI, Uvicorn, and SSE Starlette for web deployment
Additional utilities: python-dotenv, bs4, pypdf, faiss-cpu


Setup

Clone the repository.
Install dependencies: pip install -r requirements.txt
Configure environment variables in .env:
Hugging Face API tokens: HF_TOKEN, HUGGINGFACEHUB_API_TOKEN
OpenAI API keys and Azure endpoint: OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_VERSION, AZURE_DEPLOYMENT_NAME
LangSmith settings for monitoring: LANGSMITH_ENDPOINT, LANGCHAIN_API_KEY, LANGSMITH_PROJECT
Run the Jupyter notebook 1_Langchain_And_Huggingface.ipynb to test model integrations.


Usage

Execute the notebook to explore HuggingFaceEndpoint (API-based) and HuggingFacePipeline (local) model interactions.
Use LangChain's PromptTemplate and LLMChain for structured question-answering (e.g., queries about Generative AI or historical events).
Optionally, deploy the chatbot using Streamlit or FastAPI for a web-based interface.


Notes

A valid Hugging Face API token is required for serverless inference.
GPU support requires compatible hardware and drivers.
The project is designed for flexibility, supporting both local and cloud-based model execution.
