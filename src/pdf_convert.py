from langchain_community.document_loaders import PyPDFLoader

class Langchain_c():
    def __init__(self, file_path):
        self.loader = PyPDFLoader(file_path, extract_images=True)
    
    def get_pages(self):
        return self.loader.load()
