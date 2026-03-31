from fastapi import APIRouter, UploadFile, File
import shutil
from services.rag_pipeline import process_pdf

router = APIRouter()

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    path = f"temp/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    process_pdf(path)

    return {"message": "PDF processed successfully"}