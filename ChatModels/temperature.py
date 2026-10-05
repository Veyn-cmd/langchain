from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv


load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id= "ibm-granite/granite-4.2-3b",
    task = 'text-generation',
    temperature= 1.5,
    do_sample=True
)
# 0 - same kind of input
# 1 - creative different answer

model = ChatHuggingFace(llm=llm)
result = model.invoke('write a 4 line rhyme on ferrari car')
print(result.content)