# -*- coding: utf-8 -*-
# 导入Flask类
import os
from flask import Flask, jsonify
from flask import request


#实例化，可视为固定格式
app = Flask(__name__)

@app.route('/hello', methods=["get"])
def hello():
    print("hello world")
    return "hello world succeed"

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host="127.0.0.1", port=5000, debug=False
    
    
    app.run(host="127.0.0.1", port=9090)
