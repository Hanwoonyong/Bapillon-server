#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, Response, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from home import image_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is my app server'

# 首页接口
@app.route('/home', methods=['GET'])
def get_home():
    return jsonify({'data': image_file()})

# 获取图片接口
@app.route("/image")
def get_image():
    id = request.args.get('id')
    image = file("./images/{}.jpeg".format(id))
    resp = Response(image, mimetype="image/jpeg")
    return resp


if __name__ == '__main__':
    app.run(host='192.168.2.101', debug=True)
