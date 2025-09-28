import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()


def common():

    for k in (
        "OPENAI_API_KEY",
        "DATABASE_URL",
        "PG_VECTOR_COLLECTION_NAME",
        "OPENAI_EMBEDDING_MODEL",
    ):
        if not os.getenv(k):
            raise RuntimeError(
                f"É necessário definir a variável de ambiente {k} no arquivo .env"
            )

    embeddings = OpenAIEmbeddings(
        model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"),
    )

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True,
    )

    return store
