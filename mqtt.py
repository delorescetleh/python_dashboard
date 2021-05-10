#!/usr/bin/python
from flask import Flask
from flask_cors import CORS
from datetime import datetime
#import psycopg2
import json

app=Flask(__name__)
cors = CORS(app,resource={r"/api/*":{"origins":"*"}})
@app.route("/")
def home():
    return "this is mqtt"

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8083,debug=True)