from .core.embedder import Embedder
from .processors.pdf import PDFProcessor
from tqdm import tqdm


class VectorEx:
    def __init__(self, model_name: str = None):
        self.embedder = Embedder(model_name=model_name)
        self.processor = PDFProcessor()

    def process_pdf(self, file_path: str):
        """Process a PDF file and store its embeddings."""
        chunks = self.processor.process(file_path)
        filename = file_path.split("/")[-1]

        for i, chunk in enumerate(tqdm(chunks, desc="Processing PDF chunks")):
            self.embedder.add_texts(
            [chunk],
            [{"source": filename}],
            [f"{filename}_{i}"],
            )

    def search(self, query: str, n_results: int = 3):
        """Search through processed documents."""
        return self.embedder.search(query, n_results)
