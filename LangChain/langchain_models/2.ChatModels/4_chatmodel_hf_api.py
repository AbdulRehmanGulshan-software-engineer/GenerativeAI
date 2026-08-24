# HuggingFaceEndpoint is used when we want to use API of Hugging Face

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# here we have to give parameter named 'llm'
llm = HuggingFaceEndpoint(
    # repo_id means which hugging face model we want to use
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("Write a Python function to add two numbers")

print(result)