from PIL import Image
import pytesseract
import re

from .helper import storage_path, del_temporary_files


def convert_img_to_md(name: str, extension: str):
    fullName = name + extension

    img = Image.open(storage_path(fullName))
    text = pytesseract.image_to_string(img, lang="rus+eng")
    text = re.sub(" +", " ", text)
    text = re.sub("\n +", "\n", text)
    text = re.sub("\n\n+", "\n\n", text)

    del_temporary_files(name)
    return text
