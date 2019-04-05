from flask import *
from app import app
from app.models import functions

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

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

@app.route('/allData', methods=["GET", "POST", "DELETE"])
def allData():

    regIter = db.child('reg').get()
    showRegIter = regIter.val()
    innerRegIter = db.child('reg').child('firstSet').get()
    showInnerRegIter = innerRegIter.val()


    get_contInit = db.child('cont').get()
    show_contInit = get_contInit.val()

    # db.child("reg").child("childName").remove()
    # db.child("reg").child("newTest").remove()


    return render_template("/allData.html", showInnerRegIter=showInnerRegIter.values(), showRegIter=showRegIter.values(), showCont=show_contInit.values())

# ---------------------------------------------------------------------------------

# @app.route('/delete_article/<string:id>', methods=['DELETE'])
# def delete_x(id):
#     pass


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
    db.child("reg").child("thirdSet").push(allVals)
    initialValue = compoundData["init_val"][0]
    db.child("reg").child("thirdSet").push(initialValue)
    InterestRate = compoundData["intR"][0]
    db.child("reg").child("thirdSet").push(InterestRate)
    CompoundsPerYear = compoundData["yearC"][0]
    db.child("reg").child("thirdSet").push(CompoundsPerYear)
    AmountOfYears = compoundData["years"][0]
    db.child("reg").child("thirdSet").push(AmountOfYears)

    # db.child("reg").push(allVals, initialValue)

    initval = db.child("reg").get()
    num = initval.val()

    # memes = db.child("reg").child("oof").pu()

    return render_template('/shoData.html', ans=allVals)

# ---------------------------------------------------------------------------------
# Continuous Compound

@app.route('/contShoData', methods=["GET", "POST"])
def contShoData():
    contCompoundData = dict(request.form)
    print(contCompoundData)
    contAllVals = functions.contCompInt(contCompoundData["contInit_val"][0], contCompoundData["contIntR"][0], contCompoundData["contYears"][0])
    db.child('cont').push(contAllVals)
    contInitval = db.child("cont").get()
    num = contInitval.val()

    return render_template('/contShoData.html', t=contAllVals)


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
