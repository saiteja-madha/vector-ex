from vectorex import VectorEx

# Initialize
vex = VectorEx(model_name=None)

# Process a PDF
vex.process_pdf("/path/to/pdf")

# Search
results = vex.search("Example query", n_results=3)

# Print results
for i, (doc, metadata) in enumerate(
    zip(results["documents"][0], results["metadatas"][0])
):
    print(f"\nResult {i+1} from {metadata['source']}:")
    print(doc[:200] + "...")
