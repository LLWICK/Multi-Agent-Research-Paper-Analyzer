import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    # text = re.sub(r'[^\x00-\x7F]+', '', text)  # remove weird symbols
    return text