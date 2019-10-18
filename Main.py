from flask import Flask, render_template, request, redirect
import json
#from mysql import connector
from pymongo import MongoClient


app = Flask(__name__)

#db = connector.connect(host='localhost',user='adm',passwd='Azaleia150')

cliente = MongoClient('mongodb://127.0.0.1:27017')
db = cliente['db']

@app.route('/',methods=['GET'])
def index():
    return render_template('Main.html')

@app.route('/cadastrar', methods=['POST'])
def armazenar():
    name = request.form['name']
    email = request.form['email']
    senha = request.form['senha']



    user = db['user']
    post = {"name":name,"email":email,"senha":senha}

    user.insert_one(post)
    lista = []
    for u in user.find():
        lista.append(u)
    
    return render_template('List.html', list=lista)

app.run()