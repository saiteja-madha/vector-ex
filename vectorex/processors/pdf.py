from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document
from ..utils.chunker import DocumentChunker


class PDFProcessor:
    def __init__(self):
        self.chunker = DocumentChunker(
            chunk_size=800,
            overlap=80,
        )

    def process(self, file_path: str) -> list[Document]:
        """
        Process a PDF file and split it into chunks.
        """
        if not file_path.endswith(".pdf"):
            raise ValueError("File must be a PDF")

        loader = PyMuPDFLoader(file_path=file_path)
        documents = loader.load()

        chunks = self.chunker.split_documents(documents)
        chunks_with_ids = self.chunker.calculate_chunk_ids(chunks)
        return chunks_with_ids
