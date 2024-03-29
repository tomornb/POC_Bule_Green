# -*- coding: utf-8 -*-

import sys, csv, os

from flask import Flask, jsonify

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")
	
app = Flask(__name__)

tasks1 = [
    {
        'id': 1,
        'title': u'Service API 1',
        'description': u'Responce Service API 1', 
        'done': False
    }
]

tasks2 = [
    {
        'id': 2,
        'title': u'Service API 2',
        'description': u'Responce Service API 2.1', 
        'done': False
    },
    {
        'id': 3,
        'title': u'Service API 2',
        'description': u'Responce Service API 2.2', 
        'done': False
    }
]

@app.route('/api/task1', methods=['GET'])
def get_tasks1():
    return jsonify({'tasks1': tasks1})

@app.route('/api/task2', methods=['GET'])
def get_tasks2():
    return jsonify({'tasks2': tasks2})
	
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0' , port=5000 , debug=False)
    #app.run(port='5002')
	