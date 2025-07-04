from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")

# Validate API keys
if not all([openai_api_key, azure_endpoint, api_version, deployment_name]):
    raise ValueError("Missing one or more required environment variables for Azure OpenAI API.")

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["OPENAI_API_KEY"] = openai_api_key

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Initialize Azure OpenAI & Ollama Models
model = AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    openai_api_key=openai_api_key,
    api_version=api_version,
    deployment_name=deployment_name
)
llm = Ollama(model="llama2")

# Define prompts
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5-year-old child with 100 words.")

# Add API Routes
add_routes(app, prompt1 | model, path="/essay")
add_routes(app, prompt2 | llm, path="/poem")

# Run FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
