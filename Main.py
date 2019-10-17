from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
cliente = MongoClient('{{ YOUR CONNECT KEY MONGODB }}')
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
    
    return redirect('/')

app.run()