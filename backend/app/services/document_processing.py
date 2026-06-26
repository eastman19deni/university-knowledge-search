from dataclasses import dataclass

from fastapi import HTTPException, UploadFile, status
from starlette.concurrency import run_in_threadpool

from backend.app.services.document_parser import extract_text
from backend.app.services.text_chunker import split_text_into_chunks


@dataclass(frozen=True, slots=True)
class ProcessingResult:
    text: str
    chunks: list[str]


async def process_document(
    file: UploadFile,
    chunk_size: int,
    chunk_overlap: int,
) -> ProcessingResult:
    try:
        await file.seek(0)
        text = await run_in_threadpool(
            extract_text,
            file.file,
            file.filename or "",
        )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Could not extract text from the document",
        ) from error
    finally:
        await file.seek(0)

    if not text.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="The document does not contain extractable text",
        )

    chunks = split_text_into_chunks(
        text=text,
        chunk_size=chunk_size,
        overlap=chunk_overlap,
    )
    return ProcessingResult(text=text, chunks=chunks)
