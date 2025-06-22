from PyPDF2 import PdfWriter, PdfReader
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTFigure
from pdf2image import convert_from_path
import aspose.words as word
import os
import re

from .convert_image import convert_img_to_md
from .helper import storage_path, generate_file_name, del_temporary_files


def convert_pdf_to_md(name: str):
    fullName = name + ".pdf"
    pdf_path = storage_path(fullName)

    pdfFileObj = open(pdf_path, "rb")
    pdfReaded = PdfReader(pdfFileObj)
    return_text = ""

    for pagenum, page in enumerate(extract_pages(pdf_path)):
        pageObj = pdfReaded.pages[pagenum]
        page_elements = [(element.y1, element) for element in page._objs]
        page_elements.sort(key=lambda a: a[0], reverse=True)

        # Проверяем, страница является сканом или нет
        # Если да, то запускаем весь pdf в распознование картинки
        if len(page_elements) == 1 and isinstance(page_elements[0][1], LTFigure):
            img = page_elements[0][1]
            img.x1 = 1000
            img.y1 = 1000

            generateName = generate_file_name("cropped_image")
            cropPDFName = generateName + ".pdf"
            cropImageName = generateName + ".png"

            crop_image(img, pageObj, cropPDFName)
            convert_to_images(cropPDFName, cropImageName)
            return_text += convert_img_to_md(generateName, ".png")
            del_temporary_files(generateName)
        else:
            output = PdfWriter()
            output.add_page(pdfReaded.pages[pagenum])

            generateName = generate_file_name("page")
            bufferPdfName = generateName + ".pdf"
            bufferMdName = generateName + ".md"

            with open(storage_path(bufferPdfName), "wb") as outputStream:
                output.write(outputStream)
            doc = word.Document(storage_path(bufferPdfName))
            saveOptions = word.saving.MarkdownSaveOptions()
            saveOptions.images_folder = storage_path("")
            doc.save(storage_path(bufferMdName), saveOptions)
            return_text += "".join(open(storage_path(bufferMdName)).readlines()[3:-1])

            os.remove(storage_path(bufferMdName))
            os.remove(storage_path(bufferPdfName))
            del_temporary_files(generateName)

    pdfFileObj.close()
    del_temporary_files(name)

    return_text = re.sub("\n +", "\n", return_text)
    return_text = re.sub("\n\n+", "\n\n", return_text)
    return_text = re.sub(" +", " ", return_text)
    return return_text


def crop_image(element, pageObj, filename):
    [image_left, image_top, image_right, image_bottom] = [
        element.x0,
        element.y0,
        element.x1,
        element.y1,
    ]
    pageObj.mediabox.lower_left = (image_left, image_bottom)
    pageObj.mediabox.upper_right = (image_right, image_top)
    cropped_pdf_writer = PdfWriter()
    cropped_pdf_writer.add_page(pageObj)
    with open(storage_path(filename), "wb") as cropped_pdf_file:
        cropped_pdf_writer.write(cropped_pdf_file)


def convert_to_images(input_file, output_file):
    images = convert_from_path(storage_path(input_file))
    image = images[0]
    output_file = storage_path(output_file)
    image.save(output_file, "PNG")
