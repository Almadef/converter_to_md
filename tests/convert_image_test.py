import unittest
import shutil
from difflib import SequenceMatcher

from converter.convert_image import convert_img_to_md


class TestConvertPdf(unittest.TestCase):
    def test_convert_png_to_md(self):
        shutil.copy2("tests/test_files/png_test.png", "storage/png_test.png")
        result_md_text = convert_img_to_md("png_test", ".png")
        with open("tests/test_files/png_test.md", "r") as f:
            best_md_text = f.read()
        result = SequenceMatcher(None, result_md_text, best_md_text).ratio()
        self.assertTrue(
            result > 0.85,
            "Конвертация png документ в md дала сходство {0}".format(result),
        )

    def test_convert_jpg_to_md(self):
        shutil.copy2("tests/test_files/jpg_test.jpg", "storage/jpg_test.jpg")
        result_md_text = convert_img_to_md("jpg_test", ".jpg")
        with open("tests/test_files/jpg_test.md", "r") as f:
            best_md_text = f.read()
        result = SequenceMatcher(None, result_md_text, best_md_text).ratio()
        self.assertTrue(
            result > 0.85,
            "Конвертация jpg документ в md дала сходство {0}".format(result),
        )

    def test_convert_jpeg_to_md(self):
        shutil.copy2("tests/test_files/jpeg_test.jpeg", "storage/jpeg_test.jpeg")
        result_md_text = convert_img_to_md("jpeg_test", ".jpeg")
        with open("tests/test_files/jpeg_test.md", "r") as f:
            best_md_text = f.read()
        result = SequenceMatcher(None, result_md_text, best_md_text).ratio()
        self.assertTrue(
            result > 0.85,
            "Конвертация jpeg документ в md дала сходство {0}".format(result),
        )
