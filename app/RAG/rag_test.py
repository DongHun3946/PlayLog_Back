import os
from dotenv import load_dotenv

from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_upstage import ChatUpstage, UpstageEmbeddings
from langchain_chroma import Chroma
from langchain import hub
from langchain.chains import RetrievalQA
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# 현재 파일 기준 절대 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

upstage_embedding = UpstageEmbeddings(
    api_key=os.getenv("UPSTAGE_API_KEY"),
    model="solar-embedding-1-large"
)

# 이미 저장된 데이터 사용할 때
database = Chroma(
    collection_name="chroma-tax",
    persist_directory=os.path.join(BASE_DIR, "chroma"),
    embedding_function=upstage_embedding
)

llm = ChatUpstage(
    api_key=os.getenv("UPSTAGE_API_KEY")
)


def get_ai_message(user_message: str) -> str:
    # ------ 쿼리 날림 -------
    prompt = hub.pull("rlm/rag-prompt")

    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=database.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )

    dictionary = ["사람을 나타내는 표현 -> 거주자"]
    prompt1 = ChatPromptTemplate.from_template(f"""
        사용자의 질문을 보고, 우리의 사전을 참고해서 사용자의 질문을 변경해주세요.
        만약 변경할 필요가 없다고 판단된다면, 사용자의 질문을 변경하지 않아도 됩니다.
    
        사전 : {dictionary}
        
        질문 : {{question}}
    """)

    dictionary_chain = prompt1 | llm | StrOutputParser()

    tax_chain = {"query": dictionary_chain} | qa_chain

    ai_response = tax_chain.invoke({"question": user_message})
    return ai_response["result"]
