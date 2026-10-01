from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id= "ibm-granite/granite-4.2-3b",
    task = 'text-generation'
)


model = ChatHuggingFace(llm=llm)
result = model.invoke('what is capital of netherlands')
print(result.content)