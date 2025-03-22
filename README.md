AI Text Summarizer

This project is an AI-powered text summarization tool that leverages the BART model from Hugging Face's transformers library. It provides a web interface for users to input long texts and receive concise summaries. The backend is developed using Flask, and the frontend is built with HTML, CSS, and JavaScript.


Features
Summarizes long blocks of text into shorter, concise summaries.


Utilizes the BART model (facebook/bart-large-cnn) for state-of-the-art text summarization.


Web-based interface for easy input and output of text.


Demo
The app allows you to enter a large block of text, hit the "Summarize" button, and see the summarized version displayed on the page.


Tech Stack
Backend: Flask, Hugging Face Transformers (BART model)


Frontend: HTML, CSS, JavaScript



ML Model: BART (facebook/bart-large-cnn)


Setup Instructions
Prerequisites
Python 3.10 


Pip (Python package manager)


Steps to Install
Clone the repository:
git clone https://github.com/Swayam098/AI_TEXT_SUMMARIZER.git


Navigate to the project directory:
cd ai-text-summarizer

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install the required packages:
pip install -r requirements.txt

Running the App
Start the Flask server:
python app.py

Open your web browser and go to:
http://127.0.0.1:5000
Enter your text in the input box and click "Summarize" to see the summary.

API Endpoints
The project exposes a REST API that can be used for summarizing text programmatically.

POST /summarize
Request:

JSON: { "text": "Your long text goes here." }

Response:

JSON: { "summary": "Summarized text." }
