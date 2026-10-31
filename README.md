# Complete RAG Course

A practical, beginner-friendly course for learning how to build
Retrieval-Augmented Generation (RAG) applications with Python and LangChain.

RAG improves a language model's answers by retrieving relevant information from
your own documents and adding that information to the model's context before
generating a response.

## What you will learn

By working through this repository, you will learn how to:

- Load documents from text files and other common formats.
- Understand LangChain's `Document` structure and metadata.
- Split large documents into useful chunks.
- Create embeddings that represent the meaning of text.
- Store and search embeddings with a vector database.
- Retrieve relevant context for a user question.
- Build the basic RAG pipeline:

  ```text
  Documents -> Load -> Split -> Embed -> Store
                                      |
  Question  -> Embed -> Retrieve <----+
                         |
                         v
                  Language model -> Answer
  ```

## Project structure

```text
Complete_RAG_Course/
├── data/
│   ├── simple_1.txt       # Introductory RAG example
│   └── simple_2.txt       # Embeddings and vector search
├── notebook/
│   └── document.ipynb     # Document ingestion exercises
├── main.py                # Python entry point
├── pyproject.toml         # Project metadata and dependencies
├── requirements.txt       # pip-compatible dependency list
└── uv.lock               # Reproducible uv dependency lock file
```

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/) (recommended) or `pip`
- Jupyter-compatible support for running the notebook

The project currently focuses on document ingestion and the foundations of a
RAG pipeline. A model provider API key is not required for the introductory
document-loading exercises.

## Setup with uv

From the project directory, create the environment and install dependencies:

```powershell
uv sync
```

Activate the environment if you want to run commands directly inside it:

```powershell
.venv\Scripts\activate
```

## Setup with pip

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Start learning

1. Open [`notebook/document.ipynb`](notebook/document.ipynb).
2. Run the cells from top to bottom.
3. Begin with the `Document` example to understand page content and metadata.
4. Continue with the directory loader to load the sample files in [`data/`](data/).
5. Add your own `.txt` files to `data/` and experiment with loading them.
6. Next, practice chunking, embeddings, vector search, retrieval, and answer
   generation as those lessons are added.

When running the notebook, use this path for the current sample files:

```python
from langchain_community.document_loaders import DirectoryLoader, TextLoader

loader = DirectoryLoader(
    path="../data",
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"},
)
documents = loader.load()
```

If you open the notebook from a different working directory, adjust the
relative path so it points to the repository's `data` folder.

## Run the Python entry point

The current entry point is a small environment check:

```powershell
uv run python main.py
```

It should print:

```text
Hello from complete-rag-course!
```

The main RAG exercises currently live in the notebook and will be built into
the Python entry point as the course progresses.

## Sample data

The two included files are intentionally short and easy to inspect:

- [`data/simple_1.txt`](data/simple_1.txt) explains the purpose of RAG.
- [`data/simple_2.txt`](data/simple_2.txt) explains embeddings and vector
  similarity.

Short documents make it easier to see exactly what a loader returns before
moving on to larger files and more advanced retrieval strategies.

## Useful commands

```powershell
# Install or update the locked environment
uv sync

# Run the Python entry point
uv run python main.py

# Launch Jupyter
uv run jupyter notebook
```

## Troubleshooting

### `ModuleNotFoundError`

Make sure the virtual environment is active, or run the command through uv:

```powershell
uv run python main.py
```

### The notebook cannot find the data files

Relative paths are resolved from the notebook's working directory. Start
Jupyter from the repository root and use `../data` when the notebook is inside
the `notebook` folder. If your editor uses a different working directory,
update the loader path accordingly.

### Text encoding errors

Save text files as UTF-8 and keep the loader configuration:

```python
loader_kwargs={"encoding": "utf-8"}
```

## Contributing to your own learning

Try changing one part of the pipeline at a time. For each experiment, record:

- Which documents were loaded.
- How the documents were split.
- Which retrieval method was used.
- Whether the retrieved context actually answered the question.

This makes it easier to understand why a RAG application succeeds or produces
an incomplete answer.

## License

This repository is intended for educational use. Add a project-specific
license before redistributing it.
