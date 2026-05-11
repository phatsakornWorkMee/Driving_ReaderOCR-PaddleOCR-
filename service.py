from flask import Flask , request ,jsonify, request_finished, request_started
from main import Pathfile , OCR , Jsonfile
#import time
import cv2
app = Flask(__name__)
import requests

@app.route("/ServerStatus")
def ServerConnectionStatus():
    return jsonify({"status": "PaddleOCR Server is Connected."}), 200

@app.route("/paddleOCR", methods=['POST'])
def run_paddleOCR():
    json_data = request.get_json(silent=True)
    print("Content-Type:", request.content_type)
    print("Files:", request.files)
    
    if request.files.get('image'):
        image_case = "case3"
        img_file = request.files['image']
        print(f"File_NAME : {img_file}")
        Jsonfile.savefile(image_case,img_file)
        return jsonify({"result": "connect"}), 200
    
    if json_data and request.get_json().get('url'):
        image_case = "case1"
        img_file = request.files['imageX']
        Jsonfile.savefile(image_case,img_file)
        return jsonify({"result": "connect"}), 200
    
    else:
        return jsonify({"result": "disconnect"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)
