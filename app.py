from flask import Flask, render_template, request
from utilities.loading import load_pdf
from utilities.chunking import chunker
from utilities.embedding import embedding
from utilities.retriving import retriving
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', response=None)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if 'uploads' not in os.listdir():
        os.makedirs('uploads')
    file_path = f'uploads/{file.filename}'
    file.save(file_path)

    docs = load_pdf(file_path)
    chunks = chunker(docs)
    embedding(chunks)

    return render_template('retriver.html', response='File uploaded successfully.')

@app.route('/retrive', methods=['POST'])
def retrive():
    query = request.form['query']
    response = retriving(query)
    return render_template('retriver.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
