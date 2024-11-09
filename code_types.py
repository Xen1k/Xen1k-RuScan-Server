
from enum import IntEnum

class CodeType(IntEnum):
    UNKNOWN = 0
    QR = 1
    DATAMATRIX = 2
    BARCODE = 3

class DecodedEntity:
    def __init__(self, text, type):
        self.text = text
        self.type = type
    
    text = ""
    type = CodeType.UNKNOWN

    def to_dict(self):
        return {"text": self.text, "type": self.type}