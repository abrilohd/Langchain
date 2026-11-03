   # Complete RAG Course

   Senior AI Engineer Portfolio Project | Retrieval Augmented Generation with LangChain

   This repository is a practical, portfolio-ready implementation of a Retrieval-Augmented Generation (RAG) system built in Python. It demonstrates the core workflow of modern AI applications: ingest documents, split and embed them, store vector representations, retrieve semantically relevant context, and ground LLM responses in domain-specific information.

   The project reflects the kind of engineering work I focus on as a senior AI engineer: clean modular architecture, reproducible setup, vector search experimentation, and production-oriented design patterns for AI systems.

   ## Current status

   This repository is no longer just a learning example. It is a functioning RAG prototype and engineering sample with the following implemented capabilities:

   - Document ingestion from PDF, TXT, CSV, Excel, SQL, and JSON-like sources
   - LangChain document processing and chunking workflows
   - Embedding generation using sentence-transformers
   - Vector storage with FAISS
   - Metadata-aware search and retrieval
   - Groq-compatible LLM integration path
   - Notebook-based experimentation and pipeline exploration
   - Modular project structure suitable for extension into a production-ready AI assistant

   ## Why this project matters

   RAG systems are one of the most valuable patterns in applied AI today because they connect foundation models to enterprise knowledge without retraining the model. This repo showcases the engineering fundamentals behind that pattern:

   - Data ingestion and normalization
   - Chunking strategies for long-form documents
   - Semantic indexing and retrieval
   - Prompt grounding for better answer quality
   - Practical experimentation with model and retrieval choices

   ## Architecture

   ```text
   Documents
     -> Loaders (PDF, TXT, CSV, Excel, etc.)
     -> Chunking
     -> Embeddings
     -> Vector Store (FAISS)
     -> Retrieval
     -> LLM Context Assembly
     -> Answer Generation
   ```

   This is the foundation of a grounded AI system: the model answers from retrieved context instead of relying only on its internal memory.

   ## Tech stack

   - Python
   - LangChain and LangChain Community
   - SentenceTransformers
   - FAISS
   - ChromaDB
   - PyMuPDF / PyPDF
   - scikit-learn
   - Groq LLM integration
   - Jupyter notebooks

   ## Project structure

   ```text
   Complete_RAG_Course/
   ├── app.py                 # Main application entry point for vectorized document search
   ├── main.py                # Lightweight startup / environment validation entry
   ├── data/
   │   ├── pdf/               # PDF source documents for retrieval examples
   │   ├── text_file/         # Plain-text sample documents
   │   └── vector_store/      # Local vector store artifacts
   ├── faiss_store/           # Persisted FAISS index and metadata
   ├── notebook/
   │   ├── document.ipynb     # Exploratory notebook for document ingestion
   │   └── pdf_loader.ipynb   # PDF handling experiments
   ├── src/
   │   ├── data_loader.py     # Multi-format document loading pipeline
   │   ├── embedding.py        # Embedding and chunking logic
   │   ├── search.py          # Retrieval and LLM summarization logic
   │   ├── vectorstore.py     # FAISS vector database wrapper
   │   └── __init__.py
   ├── pyproject.toml         # Project metadata and dependencies
   ├── requirements.txt       # pip install dependencies
   ├── uv.lock                # Reproducible lock file for uv
   ├── .env                   # Local environment variables (not committed)
   └── README.md              # Project overview and portfolio documentation
   ```

   ## What this project demonstrates

   This repository presents the following senior-level AI engineering competencies:

   - Building data pipelines for unstructured knowledge sources
   - Designing retrieval workflows for grounded AI systems
   - Managing embedding and vector search infrastructure
   - Creating modular, extensible Python code for AI applications
   - Structuring experimentation around real-world knowledge retrieval
   - Preparing a portfolio project that shows depth beyond toy demos

   ## Quick start

   ### 1. Clone and install

   ```powershell
   git clone <repository-url>
   cd Complete_RAG_Course
   python -m venv .venv
   .venv\Scripts\activate
   python -m pip install -r requirements.txt
   ```

   ### 2. Or use uv

   ```powershell
   uv sync
   .venv\Scripts\activate
   ```

   ### 3. Run the app

   ```powershell
   uv run python app.py
   ```

   This builds or loads the FAISS index and prepares the repository for semantic search and retrieval workflows.

   ## Example workflow

   ```python
   from src.data_loader import load_all_documents
   from src.embedding import EmbeddingPipeline
   from src.vectorstore import FaissVectorStore

   # Load content
   texts = load_all_documents("data")

   # Create vector store
   pipeline = EmbeddingPipeline()
   chunks = pipeline.chunk_documents(texts)
   embeddings = pipeline.embed_chunks(chunks)

   store = FaissVectorStore("faiss_store")
   store.add_embeddings(embeddings, [chunk.metadata for chunk in chunks])
   store.save()
   ```

   ## Portfolio positioning

   This project is positioned as a demonstration of applied AI engineering skills:

   - AI system design for retrieval-grounded interactions
   - Data engineering for document-based knowledge systems
   - Python development for ML and LLM workflows
   - Vector search and semantic retrieval fundamentals
   - Practical understanding of how AI systems are built beyond prompt engineering

   ## Future improvements

   The next evolution of this project would include:

   - Hybrid retrieval combining semantic and keyword search
   - Better metadata filtering and source attribution
   - API layer for QA over documents
   - LangGraph orchestration for multi-step reasoning
   - Evaluation pipeline for retrieval quality and answer relevance
   - Streamlit or FastAPI front end for a user-facing demo

   ## Notes

   This repository is designed as a working technical portfolio artifact and a practical foundation for building production-grade RAG applications. It balances conceptual clarity with implementation depth and can be extended into a real document Q&A system, internal knowledge assistant, or enterprise search prototype.

   ## License

   This project is intended for portfolio, learning, and engineering experimentation. If you plan to reuse or redistribute it, add a project-specific license to match your intended use case.
