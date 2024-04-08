from mistral import Mistral_c
from langchain_community.document_loaders import PyPDFLoader
from pdf_convert import Langchain_c
import os

if __name__ == "__main__":
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY not found in environment variables.")
    langchain = Langchain_c("./pdf/10.pdf")
    mistral = Mistral_c(api_key)
    user_input = "what is the best cheese in french"
    pdf_txt = langchain.get_pages()
    prompt_response = mistral.prompt(pdf_txt[0].page_content + "shorten pdf please")
    mistral.print_prompt(prompt_response)