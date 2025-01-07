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
        
        file_name = file_path.split("/")[-1]
        print(f"📄 Processing PDF: {file_name} 🚀")

        loader = PyMuPDFLoader(file_path=file_path)
        documents = loader.load()
        print("Number of pages:", len(documents))

        chunks = self.chunker.split_documents(documents)
        print(f"Number of chunks: {len(chunks)}")

        return chunks
