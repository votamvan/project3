from datetime import datetime
start_time = datetime.now()

import sys, traceback
import json
import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from flask import send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
# internal import
from config import UPLOAD_FOLDER, UPLOAD_FORM, ALLOWED_EXTENSIONS, MAX_CONTENT_LENGTH
from models.resnet_gradcam import create_resnet_gradcam

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# dummy API
API_RETURN = dict(
    API_ERROR = {"status": "api error"},
    FILE_ERROR = {"status": "error", "message": "file not found"},
    API_DETECT = {
    "status": "success",
    "data": [
            {
                "bbox": [0, 0, 50, 70],
                "class": "slipper",
                "score": 0.83
            },
            {
                "bbox": [10, 20, 100, 200],
                "class": "boots",
                "score": 0.9
            }
        ]
    }
)

# real API
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET': return UPLOAD_FORM
    filename = get_file_upload(request)
    if not filename:
        flash('No file upload')
        return redirect(request.url)
    output_fname = create_resnet_gradcam(filename)
    return redirect(url_for('uploaded_file', filename=output_fname))

@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/api/v0/detect', methods=['POST'])
def detect(**kargs):
    filename = get_file_upload(request)
    if not filename: return jsonify(API_RETURN["FILE_ERROR"])
    return jsonify(API_RETURN["API_DETECT"])

@app.route('/api/v0/gradcam', methods=['POST'])
def gradcam(**kargs):
    filename = get_file_upload(request)
    if not filename: return jsonify(API_RETURN["FILE_ERROR"])
    output_fname = create_resnet_gradcam(filename)
    return jsonify({
        "status": "success",
        "data": f"{request.host_url}{url_for('uploaded_file', filename=output_fname)}"
    })

def get_file_upload(request):
    def _allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    if 'file' not in request.files: return None
    file = request.files['file']
    if file.filename == '': return None
    if not _allowed_file(file.filename): return None
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return filename


end_time = datetime.now()
print(f"Server started at {end_time.strftime('%Y-%m-%d %H:%M:%S')}, loading time = {end_time - start_time}")
app.run(host='0.0.0.0')
