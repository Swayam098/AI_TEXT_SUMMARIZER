import re

# Function to clean and preprocess text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'\[.*?\]', '', text)  # Remove text inside brackets (e.g., citations)
    return text.strip()
