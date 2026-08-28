from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it:featherless-ai",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    # it is a static prompt
    template='Give me the name,age,city of a fictional person \n {format_instruction}',
    input_variables=[],
    # below one is called partial because it filled before runtime
    partial_variables={'format_instruction':parser.get_format_instructions}
)

# prompt = template.format()
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)


# instead build this pipeline using chain
chain = template | model | parser

result = chain.invoke({})

print(result)
print(type(result))