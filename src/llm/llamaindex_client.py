import os, pinecone
from llama_index import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
)
from llama_index.vector_stores import PineconeVectorStore
from src.llm.base import load_yaml

_conf = load_yaml("config/model_config.yaml")["llamaindex"]

# initialize pinecone once
pinecone.init(
    api_key=os.getenv(_conf["pinecone_api_key_env"]),
    environment=_conf["pinecone_env"]
)
_index = pinecone.Index(_conf["pinecone_index"])
vector_store = PineconeVectorStore(pinecone_index=_index)

async def generate_with_llamaindex(prompt: str) -> str:
    # ingest if empty
    docs = SimpleDirectoryReader("data/embeddings").load_data()
    index = GPTVectorStoreIndex.from_documents(docs, vector_store=vector_store)
    query_engine = index.as_query_engine()
    return query_engine.query(prompt).response
