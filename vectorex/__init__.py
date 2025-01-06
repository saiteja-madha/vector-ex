from .core.embedder import Embedder
from .processors.pdf import PDFProcessor


class VectorEx:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.embedder = Embedder(model_name=model_name)
        self.processor = PDFProcessor()

    def process_pdf(self, file_path: str):
        """Process a PDF file and store its embeddings."""
        chunks = self.processor.process(file_path)
        self.embedder.add_documents(chunks)

    def search(self, query: str, n_results: int = 3):
        """Search through processed documents."""
        return self.embedder.search(query, n_results)
