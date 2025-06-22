from pydantic import BaseModel


class ConverterBase64Request(BaseModel):
    file_base64: str
    ext: str
