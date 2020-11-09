# -*- coding: utf-8 -*-
# 导入Flask类
import os
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS


#实例化，可视为固定格式
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/hello', methods=["get"])
def hello():
    print("hello world")

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host="127.0.0.1", port=5000, debug=False
    
    
    app.run(host="127.0.0.1", port=5000)
