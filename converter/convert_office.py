import aspose.words as word
import aspose.cells as cell
from xls2xlsx import XLS2XLSX

from .helper import storage_path, del_temporary_files


def convert_doc_docx_to_md(name: str, extension: str):
    fullName = name + extension
    mdName = name + ".md"

    doc = word.Document(storage_path(fullName))
    saveOptions = word.saving.MarkdownSaveOptions()
    saveOptions.images_folder = storage_path("")
    doc.save(storage_path(mdName), saveOptions)
    md = "".join(open(storage_path(mdName)).readlines()[3:-1])

    del_temporary_files(name)
    return md


def convert_xls_to_md(name: str):
    fullName = name + ".xls"

    # есть проблема с xls файлами, поэтому переводим их в xlsx
    x2x = XLS2XLSX(storage_path(fullName))
    x2x.to_xlsx(storage_path(name + ".xlsx"))

    return convert_xlsx_to_md(name)


def convert_xlsx_to_md(name: str):
    fullName = name + ".xlsx"
    mdName = name + ".md"

    xls = cell.Workbook(storage_path(fullName))
    xls.save(storage_path(mdName))
    md = "".join(open(storage_path(mdName)).readlines()[0:-1])

    del_temporary_files(name)
    return md
