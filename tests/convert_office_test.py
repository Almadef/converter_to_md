import unittest
import shutil
from difflib import SequenceMatcher

from converter.convert_office import (
    convert_doc_docx_to_md,
    convert_xls_to_md,
    convert_xlsx_to_md,
)


class TestConvertOffice(unittest.TestCase):
    def test_convert_doc_to_md(self):
        shutil.copy2("tests/test_files/doc_test.doc", "storage/doc_test.doc")
        result_md_text = convert_doc_docx_to_md("doc_test", ".doc")
        with open("tests/test_files/doc_test.md", "r") as f:
            best_md_text = f.read()
        result = SequenceMatcher(None, result_md_text, best_md_text).ratio()
        self.assertTrue(
            result > 0.95, "Конвертация doc в md дала сходство {0}".format(result)
        )

    def test_convert_docx_to_md(self):
        shutil.copy2("tests/test_files/docx_test.docx", "storage/docx_test.docx")
        result_md_text = convert_doc_docx_to_md("docx_test", ".docx")
        with open("tests/test_files/docx_test.md", "r") as f:
            best_md_text = f.read()
        result = SequenceMatcher(None, result_md_text, best_md_text).ratio()
        self.assertTrue(
            result > 0.95, "Конвертация docx в md дала сходство {0}".format(result)
        )

    def test_convert_xls_to_md(self):
        shutil.copy2("tests/test_files/xls_test.xls", "storage/xls_test.xls")
        result_md_text = convert_xls_to_md("xls_test")
        with open("tests/test_files/xls_test.md", "r") as f:
            best_md_text = f.read()
        result = SequenceMatcher(None, result_md_text, best_md_text).ratio()
        self.assertTrue(
            result > 0.95, "Конвертация xls в md дала сходство {0}".format(result)
        )

    def test_convert_xlsx_to_md(self):
        shutil.copy2("tests/test_files/xlsx_test.xlsx", "storage/xlsx_test.xlsx")
        result_md_text = convert_xlsx_to_md("xlsx_test")
        with open("tests/test_files/xlsx_test.md", "r") as f:
            best_md_text = f.read()
        result = SequenceMatcher(None, result_md_text, best_md_text).ratio()
        self.assertTrue(
            result > 0.95, "Конвертация xlsx в md дала сходство {0}".format(result)
        )
