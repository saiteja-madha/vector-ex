from PyPDF2 import PdfReader
from tqdm import tqdm
from ..utils.chunker import TextChunker


class PDFProcessor:
    def __init__(self):
        self.chunker = TextChunker()

    def process(self, file_path: str) -> list:
        """Process a PDF file and return chunks of text."""
        reader = PdfReader(file_path)
        text = ""
        for page in tqdm(reader.pages, desc="Chunking PDF"):
            text += page.extract_text()
        return self.chunker.chunk(text)
