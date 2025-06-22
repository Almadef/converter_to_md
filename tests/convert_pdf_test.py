import unittest
import shutil
from difflib import SequenceMatcher

from converter.convert_pdf import convert_pdf_to_md


class TestConvertPdf(unittest.TestCase):
    def test_convert_pdf_document_to_md(self):
        shutil.copy2(
            "tests/test_files/pdf_document_test.pdf", "storage/pdf_document_test.pdf"
        )
        result_md_text = convert_pdf_to_md("pdf_document_test")
        with open("tests/test_files/pdf_document_test.md", "r") as f:
            best_md_text = f.read()
        result = SequenceMatcher(None, result_md_text, best_md_text).ratio()
        self.assertTrue(
            result > 0.95,
            "Конвертация pdf документ в md дала сходство {0}".format(result),
        )

    def test_convert_pdf_image_to_md(self):
        shutil.copy2(
            "tests/test_files/pdf_image_test.pdf", "storage/pdf_image_test.pdf"
        )
        result_md_text = convert_pdf_to_md("pdf_image_test")
        with open("tests/test_files/pdf_image_test.md", "r") as f:
            best_md_text = f.read()
        result = SequenceMatcher(None, result_md_text, best_md_text).ratio()
        self.assertTrue(
            result > 0.85,
            "Конвертация pdf контейнера картинок в md дала сходство {0}".format(result),
        )
