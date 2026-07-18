import os
import shutil

from pathlib import Path

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException

from services.knowledge_service import KnowledgeService


router = APIRouter(

    prefix="/knowledge",

    tags=["Knowledge Base"]

)


UPLOAD_FOLDER = "knowledge_base"

os.makedirs(

    UPLOAD_FOLDER,

    exist_ok=True

)


@router.post("/upload")

async def upload_pdf(

    file: UploadFile = File(...)

):

    # ----------------------------
    # Validate PDF
    # ----------------------------

    if not file.filename.lower().endswith(".pdf"):

        raise HTTPException(

            status_code=400,

            detail="Only PDF files are allowed."

        )

    # ----------------------------
    # Save PDF
    # ----------------------------

    pdf_path = os.path.join(

        UPLOAD_FOLDER,

        file.filename

    )

    with open(

        pdf_path,

        "wb"

    ) as buffer:

        shutil.copyfileobj(

            file.file,

            buffer

        )

    # ----------------------------
    # Upload Knowledge
    # ----------------------------

    result = KnowledgeService.upload(

        pdf_path

    )

    return {

        "success": True,

        "filename": Path(pdf_path).name,

        **result

    }