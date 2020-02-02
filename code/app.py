from flask import Flask, render_template, request, redirect, url_for, jsonify
import tensorflow as tf
import os
import cv2
from flask_cors import CORS
from summarizer import Summarizer

app = Flask(__name__)
app.debug = True
CORS(app)

current_dir = os.path.dirname( os.path.abspath( __file__ ) )


@app.route("/")
def index():
    
    return {'test': 'success'}

@app.route("/real_bert_sum", methods=['POST'])
def real_bert_sum():
    print('bert-sum--------------------')
    data = request.get_json()
    # print(data['data'])
    
    body = data['data']
    model = Summarizer()
    result = model(body, min_length=60)
    full = ''.join(result)
    return {'answer': full }
    # return {'answer': body }
    
@app.route("/bert_sum", methods=['POST'])
def bert_sum():
    print('get-data--------------------')
    data = request.get_json()
    # print(data)
    print(current_dir + url_for('static', filename=str(data['file'])+".txt"))
    f = open( current_dir + url_for('static', filename=str(data['file'])+".txt") , "r")
    
    return { 'result': f.read() }
    # return {'answer': body }
    
    
@app.route("/review", methods=['POST'])
def review():
    print('review_data--------------------')
    data = request.get_json()
    # print(data)
    # print(current_dir + url_for('static', filename=str(data['file'])+"_1.txt"))
    f = open( current_dir + url_for('static', filename=str(data['file'])+"_1.txt") , "r")
    print(request.host) 
    img = 'http://'+request.host+'/static/img/'+str(data['file'])+".jpg"
    return { 'result': f.read(), 'img': img  }
    # return {'answer': body }

@app.route("/getClass", methods=['POST'])
def get_class():
    model_path = current_dir + url_for('static', filename="cifar10.h5")
    img_path = current_dir + url_for('static', filename="img.png")
    prediction = predict(model_path, img_path)
    return jsonify(resp=prediction)


if __name__ == "__main__":
   app.run(port='5000')