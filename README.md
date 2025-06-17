# DocuMind RAG Builder

A powerful and flexible Retrieval-Augmented Generation (RAG) system that allows you to build custom knowledge bases from your documents. Upload PDFs and other documents to create an intelligent question-answering system that provides accurate, context-aware responses based on your document content.

## Key Features

- 📄 Document Upload: Support for PDF documents
- 🔍 Smart Text Chunking: Intelligent document splitting for optimal context preservation
- 🧠 Vector Embeddings: Advanced document embedding using state-of-the-art models
- 💾 FAISS Vector Store: Fast and efficient similarity search
- 🤖 RAG Pipeline: Seamless integration of retrieval and generation
- 🌐 Web Interface: User-friendly Flask-based web application

## Project Structure

```
rag_builder/
├── app.py              # Main Flask application
├── index.py            # Core indexing functionality
├── templates/          # HTML templates
├── uploads/            # Document storage
├── utilities/          # Helper modules
│   ├── chunking.py    # Text chunking utilities
│   ├── embedding.py   # Document embedding
│   ├── loading.py     # Document loading
│   └── retriving.py   # Vector retrieval
└── vectorstore/       # FAISS index storage
```

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Visit `http://localhost:5000` in your browser

## License

MIT License 