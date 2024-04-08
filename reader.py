#!/usr/bin/env python3
##
# HACKATHON, 2024
# reader (.py)
# File description:
# PDF reader using langchain
##

import os
import re
import fitz
import requests

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page in document:
        text += page.get_text()
    return text

def find_binary_name(text):
    match = re.search(r'binary name:\s*(.+)', text, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        return "Binary name not found."

def summarize_text(text, mistral_key):
    headers = {
        "Authorization": f"Bearer {mistral_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "mistral-small-latest",
        "messages": [
            {"role": "user", "content": text[:4096]}
        ],
        "temperature": 0.7,
        "top_p": 1,
        "max_tokens": 512,
        "stream": False,
        "safe_prompt": False,
        "random_seed": None
    }
    response = requests.post("https://api.mistral.ai", json=data, headers=headers)    
#    if response.status_code == 200:
 #       result = response.json()
  #      return result.get("choices", [{}])[0].get("text", "")
   # else:
    #    return "Error: " + response.text
    return "Summary feature is currently unavailable."

def main():
    pdf_path = "exemple.pdf"
    mistral_key = os.getenv('MISTRAL_API_KEY')
#   bash command to import you mistral API key:
#   export MISTRAL_API_KEY="your_mistral_api_key"

    pdf_text = extract_text_from_pdf(pdf_path)
    binary_name = find_binary_name(pdf_text)

    print("Binary Name:", binary_name)

if __name__ == "__main__":
    main()