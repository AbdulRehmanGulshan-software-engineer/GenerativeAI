from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# initialize the model
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# cretae a prompt template
prompt = PromptTemplate(
    template="Suggest a catch blog title about {topic}.",
    input_variables=["topic"]
)

# define the input
topic = input('Enter a topic : ')

# format prompt manually using PromptTemplate
formatted_prompt = prompt.format(topic = topic)

# call the LLM directly
blog_title = llm.predict(formatted_prompt)

# print the output
print("Generated Blog Title", blog_title)