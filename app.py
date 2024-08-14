from flask import Flask, request, flash, jsonify
import os
import random
from pprint import pprint
from flask_pymongo import PyMongo
from dotenv import load_dotenv
load_dotenv()
import json


print(os.getenv("API_KEY"))
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MONGO_URI'] = "mongodb://localhost:27017/pymongo"

mongo = PyMongo(app)

@app.route('/upload-image', methods=['POST'])
def upload_image():
   file = request.files['file']
   file_path = os.path.join(app.config['UPLOAD_FOLDER'],f"{str(random.randrange(1,999999999))+file.filename}")
   file.save(file_path)
   return "saved"

@app.route('/posts', methods=['POST', 'GET'])
def postshandler():
    # pprint(request.method, 'method')
    posts = mongo.db.posts
    if request.method == 'POST':
        print("POST")
        name = request.form.get('name')
        roll = request.form.get('roll')
        posts.insert_one({
            "name": name,
            "roll": roll
        })
        return {"message":"post created"}
    if request.method == 'GET':
        print("GET")
        result = json.dumps(list(posts.find(filter=["name"])), default=str)
        return jsonify(result)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=3000, debug=True)

