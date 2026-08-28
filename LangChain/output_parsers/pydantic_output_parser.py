from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_classic.output_parsers.structured import StructuredOutputParser , ResponseSchema
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it:featherless-ai",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser
final_result = chain.invoke({'place':'Pakistani'})
print(final_result)