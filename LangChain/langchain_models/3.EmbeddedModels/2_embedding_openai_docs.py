from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=32
)

# create list as document for now
documents = [
    "Islamabad is the capital of Pakistan",
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

# embedding.embed_documents() will return us vector of 32 dimensions
result = embedding.embed_documents(documents)

print(str(result))