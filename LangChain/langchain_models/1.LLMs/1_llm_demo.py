# Note: LLMs have become old , now no one use LLMs, but still in this i will see how to work with them

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

# calling invoke function of object(llm)
result = llm.invoke("What is the capital of Pakistan")

print(result)