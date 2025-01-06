import os
import shutil
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_PATH = "./chroma_db"


class Embedder:
    def __init__(self, model_name: str):
        self.embedding_function = HuggingFaceEmbeddings(model_name=model_name)
        self.db = Chroma(
            collection_name="documents",
            persist_directory=CHROMA_PATH,
            embedding_function=self.embedding_function,
        )

    def clear_database():
        if os.path.exists(CHROMA_PATH):
            shutil.rmtree(CHROMA_PATH)

    def add_documents(self, chunks: list[Document]):
        # Get existing document IDs.
        existing_items = self.db.get(include=[])
        existing_ids = set(existing_items["ids"])
        print(f"Number of existing documents in DB: {len(existing_ids)}")

        # Only add documents that don't exist in the DB.
        new_chunks: list[Document] = []
        for chunk in chunks:
            if chunk.metadata["id"] not in existing_ids:
                new_chunks.append(chunk)

        if len(new_chunks) == 0:
            print("No new documents to add.")
            return

        print(f"Adding {len(new_chunks)} new documents to the DB.")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        self.db.add_documents(documents=new_chunks, ids=new_chunk_ids)

    def search(self, query: str, n_results: int = 3):
        results = self.db.similarity_search(query=query, k=n_results)
        return results
