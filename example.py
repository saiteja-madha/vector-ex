from vectorex import VectorEx

# Initialize
vex = VectorEx(model_name=None)

# Process a PDF
vex.process_pdf("/path/to/pdf")

# Search
results = vex.search("Example query", n_results=3)

# Print results
for doc, score in results:
    source = doc.metadata.get("id", "Unknown")
    context = doc.page_content
    print(f"Source: {source}\nScore: {score}\nContext:\n{context}\n\n---\n")