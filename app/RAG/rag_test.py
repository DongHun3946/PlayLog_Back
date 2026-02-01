import os
from dotenv import load_dotenv

from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_upstage import ChatUpstage, UpstageEmbeddings
from langchain_chroma import Chroma
from langchain import hub
from langchain.chains import RetrievalQA

load_dotenv()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=200
)

loader = Docx2txtLoader("./tax.docx")
document_list = loader.load_and_split(text_splitter=text_splitter)

upstage_embedding = UpstageEmbeddings(
    api_key=os.getenv("UPSTAGE_API_KEY"),
    model="solar-embedding-1-large"
)

# # 데이터 처음 저장할 때
# database = Chroma.from_documents(
#     documents=document_list,
#     embedding=upstage_embedding,
#     collection_name="chroma-tax",
#     persist_directory="./chroma"
# )

# # 이미 저장된 데이터 사용할 때
database = Chroma(
    collection_name="chroma-tax",
    persist_directory="./chroma",
    embedding_function=upstage_embedding
)

query = "연봉 5천만원인 직장인의 소득세는 얼마인가요?"
retrieved_docs = database.similarity_search(query, k=3)

llm = ChatUpstage(
    api_key=os.getenv("UPSTAGE_API_KEY")
)


# ------ 쿼리 날림 -------
prompt = hub.pull("rlm/rag-prompt")

qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=database.as_retriever(),
    chain_type_kwargs={"prompt": prompt}
)

ai_message = qa_chain.invoke({"query": query})
print(ai_message)
