from flask import Flask, render_template, request, jsonify
from app.summarizer import summarize_text

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')  # This will serve your index.html from the templates folder

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')

    if text:
        summary = summarize_text(text)
        return jsonify({'summary': summary})
    else:
        return jsonify({'error': 'No text provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
