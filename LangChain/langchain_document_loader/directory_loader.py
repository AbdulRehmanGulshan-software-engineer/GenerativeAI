# In actual i am not loading books folder, just writing code to do it later in any project

from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    # path of my directory
    path='books',
    # which files i want to load from that folder
    glob='*.pdf',
    # tell the loader class
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for documents in docs:
    print(documents.metadata)