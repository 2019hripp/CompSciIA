import os
from flask import *
from models import functions



app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')





@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


import pyrebase

config = {
    "apiKey": "AIzaSyCcWjlMmOWe8R4bLjsxOisZ9RK6LYzMp9o",
    "authDomain": "computer-science-ia-785c0.firebaseapp.com",
    "databaseURL": "https://computer-science-ia-785c0.firebaseio.com",
    "projectId": "computer-science-ia-785c0",
    "storageBucket": "computer-science-ia-785c0.appspot.com",
    "messagingSenderId": "295020880657",
    "serviceAccount": "serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

@app.route('/allData', methods=["GET", "POST", "DELETE"])
def allData():

    regIter = db.child('reg').get()
    showRegIter = regIter.val()

    contRegIter = db.child('cont').get()
    showContRegIter = contRegIter.val()

    return render_template("/allData.html", showRegIter=showRegIter.values(), showContRegIter=showContRegIter.values())

# ---------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------

@app.route('/enterData')
def enterData():
    return render_template("/enterData.html")

# ---------------------------------------------------------------------------------

@app.route('/contEnterData')
def contEnterData():
    return render_template("/contEnterData.html")

# ---------------------------------------------------------------------------------

@app.route('/shoData', methods=["GET", "POST"])

def shoData():
    compoundData = dict(request.form)
    print(compoundData)
    allVals = functions.compInt(compoundData["init_val"], compoundData["intR"], compoundData["yearC"], compoundData["years"])
    db.child("reg").child("fourthSet").push(allVals)
    InitialValue = compoundData["init_val"][0]
    db.child("reg").child("fourthSet").push(InitialValue)
    InterestRate = compoundData["intR"][0]
    db.child("reg").child("fourthSet").push(InterestRate)
    CompoundsPerYear = compoundData["yearC"][0]
    db.child("reg").child("fourthSet").push(CompoundsPerYear)
    AmountOfYears = compoundData["years"][0]
    db.child("reg").child("fourthSet").push(AmountOfYears)

    initval = db.child("reg").get()
    num = initval.val()

    return render_template('/shoData.html', ans=allVals)

# ---------------------------------------------------------------------------------
# Continuous Compound

@app.route('/contShoData', methods=["GET", "POST"])
def contShoData():
    contCompoundData = dict(request.form)
    print(contCompoundData)
    contAllVals = functions.contCompInt(contCompoundData["contInit_val"], contCompoundData["contIntR"], contCompoundData["contYears"])
    db.child('cont').child("setFour").push(contAllVals)
    initialValue = contCompoundData["contInit_val"][0]
    db.child('cont').child("setFour").push(initialValue)
    interestRate = contCompoundData["contIntR"][0]
    db.child('cont').child("setFour").push(interestRate)
    amountOfYears = contCompoundData["contYears"][0]
    db.child('cont').child("setFour").push(amountOfYears)

    contInitval = db.child("cont").get()
    num = contInitval.val()

    return render_template('/contShoData.html', t=contAllVals)
