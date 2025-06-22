from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
import os
import time
import base64

from .convert_office import (
    convert_doc_docx_to_md,
    convert_xls_to_md,
    convert_xlsx_to_md,
)
from .convert_pdf import convert_pdf_to_md
from .convert_image import convert_img_to_md
from .schemas import ConverterBase64Request
from .helper import storage_path

router = APIRouter(prefix="/convert", tags=["Методы для конвертации файлов"])
validExtensions = [".doc", ".docx", ".xls", ".xlsx", ".pdf", ".png", ".jpg", ".jpeg"]


@router.post("/file_to_markdown_text")
def convert_file_to_markdown_text(file: UploadFile):
    """
    Поддерживаются расширения: doc, docx, xls, xlsx, pdf, png, jpg, jpeg.
    """

    try:
        filename = str(int(time.time())) + "_" + file.filename
        name, extension = os.path.splitext(filename)
        if extension not in validExtensions:
            return JSONResponse(
                content={
                    "success": False,
                    "error": "Неподдерживаемое расширение файла",
                },
                status_code=500,
            )
        contents = file.file.read()
        with open(storage_path(filename), "wb") as f:
            f.write(contents)
    except Exception:
        return JSONResponse(
            content={"success": False, "error": "Не удалось загрузить файл"},
            status_code=500,
        )
    finally:
        file.file.close()

    try:
        match extension:
            case ".doc" | ".docx":
                md_text = convert_doc_docx_to_md(name, extension)
            case ".xls":
                md_text = convert_xls_to_md(name)
            case ".xlsx":
                md_text = convert_xlsx_to_md(name)
            case ".pdf":
                md_text = convert_pdf_to_md(name)
            case ".png" | ".jpg" | ".jpeg":
                md_text = convert_img_to_md(name, extension)
    except Exception as e:
        return JSONResponse(
            content={
                "success": False,
                "error": "Программная ошибка конвертера " + repr(e),
            },
            status_code=500,
        )

    return {"success": True, "md_text": md_text}


@router.post("/base64_to_markdown_text")
def convert_base64_to_markdown_text(request: ConverterBase64Request):
    """
    Поддерживаются расширения: doc, docx, xls, xlsx, pdf, png, jpg, jpeg.
    """

    extension = "." + request.ext
    if extension not in validExtensions:
        return JSONResponse(
            content={"success": False, "error": "Неподдерживаемое расширение файла"},
            status_code=500,
        )

    try:
        name = str(int(time.time()))
        with open(storage_path(name + extension), "wb") as f:
            f.write(base64.b64decode(request.file_base64))
    except Exception:
        return JSONResponse(
            content={"success": False, "error": "Не удалось обработать base64 строку"},
            status_code=500,
        )

    try:
        match extension:
            case ".doc" | ".docx":
                md_text = convert_doc_docx_to_md(name, extension)
            case ".xls":
                md_text = convert_xls_to_md(name)
            case ".xlsx":
                md_text = convert_xlsx_to_md(name)
            case ".pdf":
                md_text = convert_pdf_to_md(name)
            case ".png" | ".jpg" | ".jpeg":
                md_text = convert_img_to_md(name, extension)
    except Exception as e:
        return JSONResponse(
            content={
                "success": False,
                "error": "Программная ошибка конвертера " + repr(e),
            },
            status_code=500,
        )

    return {"success": True, "md_text": md_text}
