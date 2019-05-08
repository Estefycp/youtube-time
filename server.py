#!/usr/bin/python3

'''
export FLASK_APP=server.py
flask run
'''

from flask import Flask, jsonify, make_response, request, render_template, Response
import os
app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    req       = request.json
    res       = {}
    if (req == None): req = request.form


    return "p"

app.run(host='0.0.0.0', port= int(os.environ.get('PORT', 5000)))