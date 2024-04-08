from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("10.pdf", extract_images=True)
pages = loader.load()
print(pages[0].page_content)