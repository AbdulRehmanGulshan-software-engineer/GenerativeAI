from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

parser = StrOutputParser()

class Feedback(BaseModel):
    
    sentiment: Literal['positive','negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(
    pydantic_object=Feedback
)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser2
feedback = """
The overall experience was good, but a few areas could be improved. The interface felt simple and easy to navigate, although some sections took a little longer to load than expected. The responses were generally helpful and clear, but occasionally lacked enough detail. Adding more customization options and improving consistency would make the experience even better. Overall, a solid experience with room for improvement.
"""

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find sentimemt")
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': feedback})
print(result)