import PyPDF2
import os

class DocumentReader:
    filename = None
    _document = None
    _extension = ""
    _text = ""
    
    def __init__(self):
        return
    
    def convert_to_text(self):
        """ Convert the document to text
        
        Returns:
            str: The text of the document
        """
        
        convert_file_type_handlers = {
        "pdf": self._convert_pdf,
        "txt": self._convert_txt,
        }
        
        handler = convert_file_type_handlers.get(self._extension.lower(), self.unsupported_file_type)
        return handler()
        
    def _convert_pdf(self):
        text = ""
        for page in self._document.pages:
            page_text = page.extract_text()
            cleaned_text = page_text.strip().replace('\n', ' ')
            text += cleaned_text
        return text
    
    def _convert_txt(self):
        return self._document
    
    def open(self, filename):
        """ Open a document
        
        Args:
            filename (str): The name of the document to open
        """
        self.filename = filename
        self._extension = os.path.splitext(self.filename)[1][1:]
        
        open_file_type_handlers = {
        "pdf": self._open_pdf,
        "txt": self._open_txt,
        }
        
        handler = open_file_type_handlers.get(self._extension.lower(), self.unsupported_file_type)
        handler()
        
    def close(self):
        """ Close the document
        """
        self._document = None
        self._text = ""
        self.filename = ""
        self._extension = ""
    
    def _open_pdf(self):
        self._document = PyPDF2.PdfReader(self.filename)
        
    def _open_txt(self):
        with open(self.filename, 'r') as file:
            self._document = file.read()
            
    def unsupported_file_type(self):
        print(f"Unsupported file type: {self._extension}")