import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from common import common

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE") or 1000)
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP") or 150)


def get_pdf_path():
    for k in ("PDF_FILENAME",):
        if not os.getenv(k):
            raise RuntimeError(
                f"É necessário definir a variável de ambiente {k} no arquivo .env"
            )

    current_dir = Path(__file__).parent.parent
    PDF_PATH = current_dir / os.getenv("PDF_FILENAME")

    return PDF_PATH


def enriched_documents(pdf_path):
    docs = PyPDFLoader(pdf_path).load()
    splits = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP, add_start_index=False
    ).split_documents(docs)
    if not splits:
        raise SystemExit(0)
    enriched = [
        Document(
            page_content=d.page_content,
            metadata={k: v for k, v in d.metadata.items() if v not in ("", None)},
        )
        for d in splits
    ]
    ids = [f"doc-{i}" for i in range(len(enriched))]

    return enriched, ids


def ingest_pdf():
    print("Iniciando ingestão do PDF.")
    pdf_path = get_pdf_path()
    enriched, ids = enriched_documents(pdf_path)
    store = common()
    store.add_documents(enriched, ids=ids)
    print(f"PDF '{os.getenv('PDF_FILENAME')}' foi ingerido com sucesso.")


if __name__ == "__main__":
    ingest_pdf()
