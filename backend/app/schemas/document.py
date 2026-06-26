import uuid
from datetime import datetime

from pydantic import BaseModel


class DocumentUploadResponse(BaseModel):
    id: int
    uuid: uuid.UUID
    file_name: str
    file_path: str
    created_at: datetime
    extracted_characters: int
    chunks_count: int
