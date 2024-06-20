from flask import Flask, request, jsonify
import tabula
import os
import tempfile
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.pdf'):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
            file.save(temp_file.name)
            temp_file_path = temp_file.name
        
        try:
            print(f"File saved to {temp_file_path}")
            tables = tabula.read_pdf(temp_file_path, pages='all', multiple_tables=True)
            result = [table.to_json(orient='split') for table in tables]
            print("Tables extracted:", result)
        finally:
            os.remove(temp_file_path)
        
        return jsonify(result), 200
    else:
        return jsonify({'error': 'Invalid file format'}), 400

if __name__ == '__main__':
    app.run(debug=True)
