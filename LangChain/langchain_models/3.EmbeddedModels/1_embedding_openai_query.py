from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=32
)

# embedding.embed_query() will return us vector of 32 dimensions
result = embedding.embed_query("Islamabad is the capital of Pakistan.")

print(str(result))