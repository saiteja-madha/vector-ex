from setuptools import setup, find_packages

setup(
    name="vector-ex",
    version="0.1",
    description="A vector-based document search and processing system",
    author="Sai Teja Madha",
    author_email="contact@saitejamadha.dev",
    packages=find_packages(include=["vectorex", "vectorex.*"]),
    install_requires=[
        "chromadb>=0.6.0",
        "einops>=0.8.0",
        "PyPDF2>=3.0.0",
        "sentence-transformers>=3.3.0",
        "tqdm>=4.67.0",
    ],
    python_requires=">=3.12",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
)
