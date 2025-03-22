from transformers import BartTokenizer, BartForConditionalGeneration

# Function to load BART model and tokenizer
def load_model():
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    return model, tokenizer
