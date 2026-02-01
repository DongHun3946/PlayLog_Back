import numpy as np
import os

from dotenv import load_dotenv
from openai import OpenAI
from langchain_upstage import ChatUpstage


load_dotenv()

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)

    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0

    return dot_product / (norm_vec1 * norm_vec2)

upstage_client = OpenAI(
    api_key=os.getenv("UPSTAGE_API_KEY"),
    base_url="https://api.upstage.ai/v1/solar"
)

#Example1
king_embedding_response = upstage_client.embeddings.create(
    input="곤충",
    model="solar-embedding-1-large-query"
)
king_vector = np.array(king_embedding_response.data[0].embedding)

#Example2
queen_embedding_response = upstage_client.embeddings.create(
    input="개미",
    model="solar-embedding-1-large-query"
)
queen_vector = np.array(queen_embedding_response.data[0].embedding)


king_queen_similarity = cosine_similarity(king_vector, queen_vector)
print(king_queen_similarity)