from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# configure llm
HuggingFacePipeline.from_model_id(
    model_id='openai/gpt-oss-20b',
    task='text-generation',
    # option for sending keyword arguments
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm="llm")

result = model.invoke("What is the capital of Pakistan?")

print(result.content)