from flask import *
from app import app
from app.models import functions

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

@app.route('/allData', methods=["GET", "POST"])
def allData():
    getCompounds = db.child('initval').get()
    showCompound = getCompounds.val()
    return render_template("/allData.html", showCompound=showCompound)

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
    allVals = functions.compInt(compoundData["init_val"][0], compoundData["intR"][0], compoundData["yearC"][0], compoundData["years"][0])
    #number = request.form['number']
    db.child("initval").push(allVals)
    initval = db.child("initval").get()
    #num = initval.val()

    return render_template('/shoData.html', ans=allVals)

# ---------------------------------------------------------------------------------
# Continuous Compound

@app.route('/contShoData', methods=["GET", "POST"])
def contShoData():
    contCompoundData = dict(request.form)
    print(contCompoundData)
    contAllVals = functions.contCompInt(contCompoundData["contInit_val"][0], contCompoundData["contIntR"][0], contCompoundData["contYears"][0])
    db.child('contInit_val').push(contAllVals)
    # if request.method == 'POST':
        # number = request.form['number']
    initval = db.child("contInit_val").get()
    num = initval.val()

    return render_template('/contShoData.html', t=num.values())


#     contCompoundData = dict(request.form)
#     print(contCompoundData)
#     contAllVals = functions.contCompInt(contCompoundData["contInit_val"][0], contCompoundData["contIntR"][0], contCompoundData["contYears"][0])
#
#     return render_template('/contShoData.html', contAns=contAllVals)
# #
# ---------------------------------------------------------------------------------
# Login Information

    # contAllVals = functions.contCompInt(contCompoundData["contInit_val"][0], compoundData["contIntR"][0], compoundData["contYears"][0])
    #
    # return render_template('/enterData.html')
