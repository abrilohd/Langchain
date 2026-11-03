from pathlib import Path
from typing import List, Dict, Any
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    Docx2txtLoader,
    UnstructuredExcelLoader,
    JSONLoader,
)


def load_all_documents(data_dir: str) -> List[Any]:
    """
    Load all supported files from the data directory and convert to LangChain document structures.
    Supported: PDF, TXT, CSV, Excel, Word, JSON
    """
    # Use project root data folder
    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data path: {data_path}")
    documents = []

    # PDF files
    pdf_files = list(data_path.glob("**/*.pdf"))
    print(f"[DEBUG] Found {len(pdf_files)} PDF files: {[str(f) for f in pdf_files]}")
    for pdf_file in pdf_files:
        print(f"[DEBUG] Loading PDF: {pdf_file}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} PDF docs from {pdf_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load PDF {pdf_file}: {e}")

    # Text files
    txt_files = list(data_path.glob("**/*.txt"))
    print(f"[DEBUG] Found {len(txt_files)} TXT files: {[str(f) for f in txt_files]}")
    for txt_file in txt_files:
        print(f"[DEBUG] Loading TXT: {txt_file}")
        try:
            loader = TextLoader(str(txt_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} TXT docs from {txt_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load TXT {txt_file}: {e}")

    # CSV files
    csv_files = list(data_path.glob("**/*.csv"))
    print(f"[DEBUG] Found {len(csv_files)} CSV files: {[str(f) for f in csv_files]}")
    for csv_file in csv_files:
        print(f"[DEBUG] Loading CSV: {csv_file}")
        try:
            loader = CSVLoader(str(csv_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} CSV docs from {csv_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load CSV {csv_file}: {e}")

    # Excel files
    excel_files = list(data_path.glob("**/*.xlsx"))
    print(
        f"[DEBUG] Found {len(excel_files)} Excel files: {[str(f) for f in excel_files]}"
    )
    for excel_file in excel_files:
        print(f"[DEBUG] Loading Excel: {excel_file}")
        try:
            loader = UnstructuredExcelLoader(str(excel_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} Excel docs from {excel_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load Excel {excel_file}: {e}")

    # Sql files
    sql_files = list(data_path.glob("**/*.sql"))
    print(f"[DEBUG] Found {len(sql_files)} SQL files: {[str(f) for f in sql_files]}")
    for sql_file in sql_files:
        print(f"[DEBUG] Loading SQL: {sql_file}")
        try:
            loader = TextLoader(str(sql_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} SQL docs from {sql_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load SQL {sql_file}: {e}")

    return documents
