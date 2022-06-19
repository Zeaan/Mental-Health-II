from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestClassifier
import pickle

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/contact')
def about():
    return render_template("contact.html")

@app.route('/data')
def help():
    return render_template("data.html")

@app.route('/classifier', methods=['GET','POST'])
def diabetes():
    pickle_in = open("randomForestModel.pickle","rb")
    model = pickle.load(pickle_in)
    if request.method=="POST":
        Gender = float(request.form["Gender"])
        Course = float(request.form["Course"])
        Year = float(request.form["Year"])
        Age = float(request.form["Age"])
        CGPA = float(request.form["CGPA"])
        Marital_status = float(request.form["MS"])
        Treatment = float(request.form["Treatment"])
        Anxiety = float(request.form["Anxiety"])
        Panic_attack = float(request.form["PA"])
        Outcome = model.predict( [[Gender,Age,Course,Year,CGPA,Marital_status,Anxiety,Panic_attack,Treatment]] ).tolist()
        prediction = Outcome[0]
        return render_template("result.html", prediction=prediction)
    return render_template("classifier.html")

if __name__=='__main__':
    app.run(debug=True, port=8000)