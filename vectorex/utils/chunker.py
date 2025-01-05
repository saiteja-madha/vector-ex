class TextChunker:
    def __init__(self, chunk_size: int = 1000, overlap: int = 100):
        if overlap >= chunk_size:
            raise ValueError("Overlap must be less than chunk size")
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> list:
        """Split text into overlapping chunks."""
        chunks = []
        start = 0
        text_length = len(text)

        while start < text_length:
            end = min(start + self.chunk_size, text_length)
            chunks.append(text[start:end])
            start += self.chunk_size - self.overlap

        return chunks
