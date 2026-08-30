from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

prompt = PromptTemplate(
    template="Write the summary for the following poem - \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

# created loader object of TextLoader class
loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))