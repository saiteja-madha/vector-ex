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