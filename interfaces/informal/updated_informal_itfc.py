

class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))


class UpdatedInformalParserInterface(metaclass=ParserMeta):
    pass

class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text(self, full_file_path: str) -> dict:
        pass   


class EmailParserNew:
        def __init__(self):
                super().__init__()

        def load_datasource(self, path, filename):
              pass
        def extraxt_email_data(self, file_name):
              pass

print("UpdatedInformalParserInterface is a virtual base class of PdfParserNew.")
print("PdfParserNe is a subclasss".format(issubclass(PdfParserNew, UpdatedInformalParserInterface)))  


print("The EmailParer does NOT implement all the methods: {}".format(issubclass(EmailParserNew, UpdatedInformalParserInterface))) 

