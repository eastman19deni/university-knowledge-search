from pathlib import Path
from typing import BinaryIO

import pdfplumber
from docx import Document as DocxDocument


class UnsupportedDocumentTypeError(ValueError):
    pass


def extract_text(file: BinaryIO, file_name: str) -> str:
    extension = Path(file_name).suffix.lower()

    if extension == ".pdf":
        return extract_pdf_text(file)
    if extension == ".docx":
        return extract_docx_text(file)

    raise UnsupportedDocumentTypeError(
        f"Unsupported document extension: {extension}"
    )


def extract_pdf_text(file: BinaryIO) -> str:
    with pdfplumber.open(file) as pdf:
        pages = [
            text.strip()
            for page in pdf.pages
            if (text := page.extract_text())
        ]

    return "\n\n".join(pages)


def extract_docx_text(file: BinaryIO) -> str:
    document = DocxDocument(file)
    paragraphs = [
        paragraph.text.strip()
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    return "\n\n".join(paragraphs)
