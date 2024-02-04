import io
import os

from flask import Flask, request, jsonify
import base64, random
from PIL import Image


app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({"Server":"Success"})

@app.route('/save_image', methods=['POST'])
def post():
    print("request")
    payload = request.get_json(force=True)
    # print(payload)
    category = payload.get("category")
    img_data = payload.get("image")
    # print(category)
    # print(img_data)
    parent_dir = os.getcwd()
    directory = category
    path = os.path.join(parent_dir,directory)
    if not directory in os.listdir():
        os.mkdir(path)
    #directory = os.getcwd() + "/" + category + "/"
    file_name = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10)) + ".png"
    file_path = os.path.join(path,file_name)
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(img_data, "utf-8"))))
    img.save(file_path)
    return jsonify({"message": "Save successful", "error": None})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)