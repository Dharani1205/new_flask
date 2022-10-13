from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
 

app = Flask(__name__)
app.secret_key = 'your secret key'
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'DOC'
 
mysql = MySQL(app)

@app.route('/')
def home():
    if 'name' in session:
        name = session['name']
        return jsonify({'message' : 'You are logged in','name':name})
    else:
        resp = jsonify({'message' : 'unauthorized'})
        resp.status_code = 401
        return resp

@app.route('/login', methods=['POST'])
def login():
    _json = request.json
    name = _json['name']
    password = _json['password']
    print(password)
    if name and password:
        return jsonify({'message' : 'You are logged in successfully'})
    else:
        resp = jsonify({'message' : 'Bad Request - invalid credentials'})
        resp.status_code = 400 
        return resp




if __name__ =='__main__':
    app.run(debug=True)

