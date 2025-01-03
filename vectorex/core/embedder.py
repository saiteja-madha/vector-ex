from chromadb.utils import embedding_functions
import chromadb


class Embedder:
    def __init__(self, model_name: str = None):
        if model_name is None:
            self.embedding_function = embedding_functions.DefaultEmbeddingFunction()
        else:
            self.embedding_function = (
                embedding_functions.SentenceTransformerEmbeddingFunction(
                    model_name=model_name, trust_remote_code=True
                )
            )
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.get_collection()

    def get_collection(self, name: str = "documents"):
        try:
            self.client.delete_collection(name)
        except:
            pass
        return self.client.create_collection(
            name=name, embedding_function=self.embedding_function
        )

    def add_texts(self, texts: list, metadata: list, ids: list):
        self.collection.add(documents=texts, metadatas=metadata, ids=ids)

    def search(self, query: str, n_results: int = 3):
        return self.collection.query(
            query_texts=[f"search_document: {query}"], n_results=n_results
        )
