import chromadb


class ChromaClient:

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )