# VectorEx (Vector-based Extraction)

A vector-based document search and processing system

## Usage

1. Install the package using pip

```bash
pip install git+https://github.com/saiteja-madha/vector-ex.git
```

2. Create a directory with PDF files

3. Create a Python script with the following code

```python
from vectorex import VectorEx

# Initialize
vex = VectorEx()

# Process PDF files in a directory
vex.process_dir("./data")

# Search
results = vex.search("Example query", n_results=3)

# Print results
print("\n\nSearch results:")
for doc, score in results:
    source = doc.metadata.get("id", "Unknown")
    context = doc.page_content
    print(f"Source: {source}\nScore: {score}\nContext:\n{context}\n\n---\n")

```

## Development Setup

```bash
git clone https://github.com/saiteja-madha/vector-ex.git
cd vector-ex
pip install -r requirements.txt
python example.py
```
