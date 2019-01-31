from flask import *
from app import app
from app.models import compounds

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')




# data base
import pyrebase

config = {
    "apiKey": "AIzaSyCcWjlMmOWe8R4bLjsxOisZ9RK6LYzMp9o",
    "authDomain": "computer-science-ia-785c0.firebaseapp.com",
    "databaseURL": "https://computer-science-ia-785c0.firebaseio.com",
    "projectId": "computer-science-ia-785c0",
    "storageBucket": "computer-science-ia-785c0.appspot.com",
    "messagingSenderId": "295020880657",
    "serviceAccount": "app/serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

@app.route('/database', methods=["POST"])
def database():
    return render_template("/database.html")

@app.route('/shoData', methods=["GET", "POST"])
def shoData():
    # if request.method == 'POST':
    #     number = request.form['number']
    #     db.child("initval").push(number)
    #     initval = db.child("initval").get()
    #     num = initval.val()
    #     return render_template('/database.html', t=num.values())
    compoundData = dict(request.form)
    print(compoundData)
    allVals = compounds.compInt(compoundData["init_val"][0], compoundData["intR"][0], compoundData["yearC"][0], compoundData["years"][0])
    return render_template('/shoData.html', ans=allVals)
