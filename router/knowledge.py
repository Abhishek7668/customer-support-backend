# import os
# import shutil
# from pathlib import Path

# print("========== 1. knowledge.py loaded ==========")

# from fastapi import APIRouter, UploadFile, File, HTTPException

# print("========== 2. FastAPI imported ==========")

# from services.knowledge_service import KnowledgeService

# print("========== 3. KnowledgeService imported ==========")

# router = APIRouter(
#     prefix="/knowledge",
#     tags=["Knowledge Base"]
# )

# UPLOAD_FOLDER = "knowledge_base"

# os.makedirs(
#     UPLOAD_FOLDER,
#     exist_ok=True
# )

# print("========== 4. Upload folder ready ==========")


# @router.post("/upload")
# async def upload_pdf(file: UploadFile = File(...)):

#     print("========== Upload API Called ==========")

#     if not file.filename.lower().endswith(".pdf"):
#         raise HTTPException(
#             status_code=400,
#             detail="Only PDF files are allowed."
#         )

#     pdf_path = os.path.join(
#         UPLOAD_FOLDER,
#         file.filename
#     )

#     with open(pdf_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     print("========== PDF Saved ==========")

#     result = KnowledgeService.upload(pdf_path)

#     print("========== Upload Completed ==========")

#     return {
#         "success": True,
#         "filename": Path(pdf_path).name,
#         **result
#     }

from fastapi import APIRouter, UploadFile, File

router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge"]
)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    return {
        "success": True,
        "filename": file.filename
    }