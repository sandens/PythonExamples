## This is an example of an informal interface

class MyParserInterface(object):
      
      def load_datasource(self, path: str, filename: str) ->str:
          """ Load date from a given file """
          pass

      def extraxt_data(self,file_name: str):
          """ Extract data from a given datasource """
          pass

class PDFParser(MyParserInterface):
        def __init__(self):
                    super().__init__()

        def load_datasource(self, path, filename):
                    return super().load_datasource(path, filename)
        
        def extraxt_data(self, file_name):
                return super().extraxt_data(file_name)

class EmailParser(MyParserInterface):
        def __init__(self):
                super().__init__()

        def load_datasource(self, path, filename):
                return super().load_datasource(path, filename)

        def extraxt_email_data(self, file_name):
                return super().extraxt_data(file_name)                

print("Both of these report as subclasses .. BUT the EmailParsar is not")
print(issubclass(EmailParser, MyParserInterface))
print(issubclass(PDFParser, MyParserInterface))
