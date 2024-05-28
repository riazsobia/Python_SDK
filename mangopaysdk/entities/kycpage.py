from mangopaysdk.entities.entitybase import Dto
import base64


class KycPage (Dto):
    """KycPage entity
    Container for file
    file should be utf-8 encoded string
    """
    
    def __init__(self, id = None):
        # String (file base64 encoded)
        self.File = ''
        
    def LoadDocumentFromFile(self, pathToFile):
        with open(pathToFile, "rb") as file:
            bytes = base64.b64encode(file.read())
            self.File = bytes.decode("utf-8")
        return self