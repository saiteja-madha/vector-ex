from setuptools import setup, find_packages

setup(
    name="vector-ex",
    version="0.1",
    description="A vector-based document search and processing system",
    author="Sai Teja Madha",
    author_email="contact@saitejamadha.dev",
    packages=find_packages(include=['vectorex', 'vectorex.*']),
    install_requires=[
        "langchain-chroma>=0.1.4",
        "langchain-community>=0.3.14",
        "langchain-core>=0.3.29",
        "langchain-huggingface>=0.1.2",
        "langchain-text-splitters>=0.3.4",
        "PyMuPDF>=1.25.0",
        "sentence-transformers>=3.3.0",
    ],
    python_requires=">=3.12",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
)
