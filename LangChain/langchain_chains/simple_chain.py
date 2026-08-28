# prompt from user
# send it to LLM
# send output to user

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# creating prompt using prompt template
prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# parser that can give output in string
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()