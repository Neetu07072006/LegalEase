
from fastapi import APIRouter, UploadFile, File, HTTPException
from io import BytesIO
from pypdf import PdfReader
from docx import Document
from app.services.demo_analyzer import analyze_document

router = APIRouter(prefix="/api/documents", tags=["Documents"])

@router.post("/analyze")
async def analyze_uploaded_document(file: UploadFile = File(...)):
    filename = file.filename or ""
    extension = filename.lower().split(".")[-1]

    if extension not in ["pdf", "docx"]:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported."
        )

    content = await file.read()

    if not content:
        raise HTTPException(status_code=400, detail="The uploaded file is empty.")

    if len(content) > 15 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="Maximum file size is 15 MB.")

    try:
        if extension == "pdf":
            reader = PdfReader(BytesIO(content))
            pages = [
                f"[PAGE {index + 1}]\n{page.extract_text() or ''}"
                for index, page in enumerate(reader.pages)
            ]
            extracted_text = "\n\n".join(pages)
            page_count = len(reader.pages)
        else:
            document = Document(BytesIO(content))
            extracted_text = "\n".join(
                paragraph.text for paragraph in document.paragraphs
            )
            page_count = None

        if not extracted_text.strip():
            raise HTTPException(
                status_code=422,
                detail="No readable text found. Scanned PDFs require OCR."
            )

        analysis = await analyze_document(extracted_text)

        return {
            "success": True,
            "document_name": filename,
            "document_type": extension.upper(),
            "page_count": page_count,
            "word_count": len(extracted_text.split()),
            "analysis": analysis
        }

    except HTTPException:
        raise
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))
    except Exception as error:
        raise HTTPException(
            status_code=502,
            detail=f"AI analysis failed: {str(error)}"
        )
