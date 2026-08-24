from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    # this embedding model is just 90 mb we can local host it
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

text = "Islamabad is the capital of Pakistan."

vector = embedding.embed_query(text)

print(str(vector))