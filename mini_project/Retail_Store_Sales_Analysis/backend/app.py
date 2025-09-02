from flask import Flask, request, jsonify, send_file, render_template
import os
from analysis import analyze_sales

app = Flask(__name__, static_folder="../frontend", template_folder="../frontend")

# Upload and output directories
UPLOAD_FOLDER = os.path.join('backend', 'uploads')
OUTPUT_FOLDER = os.path.join('backend', 'outputs')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Call analysis function
    results = analyze_sales(filepath)

    # Validate results keys
    if not all(key in results for key in ['cleaned', 'store_summary', 'weekday_summary']):
        return jsonify({"error": "Analysis function did not return expected keys"}), 500

    return jsonify({
        "message": "Analysis completed",
        "cleaned_file": f"/download/{os.path.basename(results['cleaned'])}",
        "store_summary": f"/download/{os.path.basename(results['store_summary'])}",
        "weekday_summary": f"/download/{os.path.basename(results['weekday_summary'])}"
    })

@app.route('/download/<filename>')
def download(filename):
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
