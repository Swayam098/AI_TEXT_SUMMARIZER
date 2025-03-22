from transformers import pipeline

# Load summarization model (facebook/bart-large-cnn)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")

def summarize_text(text):
    summary = summarizer(text, max_length=50, min_length=10, do_sample=False)
    return summary[0]['summary_text']
