from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

model2 = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

# merging logic , using sequential chain
merge_chain = prompt3 | model1 | parser

# making final chain
chain = parallel_chain | merge_chain

text = """
The solar observatory stood on a quiet plateau where the air was unusually dry and clear. Every morning, researchers opened the dome before sunrise and calibrated the instruments using reference stars. The main telescope collected visible light, while a smaller instrument measured changes in solar radiation. Over several months, the team noticed that periods of increased solar activity sometimes coincided with stronger radio signals in the upper atmosphere. However, the relationship was not perfectly consistent, so the researchers began recording additional variables such as atmospheric pressure, humidity, and seasonal temperature.

One researcher suggested that the differences might be caused by the Earth's magnetic field interacting with charged particles released by the Sun. Another argued that local atmospheric conditions could explain some of the measurements. To investigate, the team divided their observations into groups based on weather conditions and compared measurements collected at different times of day. They also repeated several experiments to determine whether the same patterns appeared consistently.

After analyzing the data, the researchers concluded that scientific observations become more reliable when measurements are repeated, environmental factors are controlled, and alternative explanations are considered. They planned a larger experiment for the following year using improved sensors and a longer observation period.
"""

# invoke the chain
result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()