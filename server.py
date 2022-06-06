from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
import os
import sys
from sympy import Id

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Hemodialysis.db'

db = SQLAlchemy(app)


class Patients(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    FullName = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(50), unique=True)
    Phone = db.Column(db.Integer, primary_key=True)
    TreatingDoctor = db.Column(db.String(100), nullable=False)
    BloodType = db.Column(db.String(2), nullable=False)
    Password = db.Column(db.String(50))
    DateOfBirth = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Name %s>' % self.FristName


'''
import pickle
from sklearn.preprocessing import StandardScaler
'''


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home/')
def home():
    return render_template('home.html')


@app.route('/Login.html/', methods=["POST", "GET"])
def Login():
    return render_template('Login.html')


@app.route('/Admin-registration.html/', methods=["POST", "GET"])
def AdminRegistration():
    return render_template('Admin-registration.html')


@app.route('/Doctor-registration.html/', methods=["POST", "GET"])
def DoctorRegistration():
    return render_template('Doctor-registration.html')


@app.route('/Patient-registration.html/', methods=['POST', 'GET'])
def PatientRegistration():
    title = "Our Patients list"

    if request.method == "POST":
        P_name = request.form['FullName']
        P_ID = request.form['SSN']
        P_Email = request.form['Mail']
        P_Phone = request.form['Phone']
        P_TreatingDoctor = request.form['TreatingDoctor']
        P_BloodType = request.form['BloodType']
        P_DateOfBirth = request.form['DOB']
        P_Password = request.form['Password']
        new_patient = Patients(Id=P_ID, FullName=P_name, Email=P_Email, Phone=P_Phone,
                               TreatingDoctor=P_TreatingDoctor, BloodType=P_BloodType, DateOfBirth=P_DateOfBirth, Password=P_Password)
        try:
            db.session.add(new_patient)
            db.session.commit()
            return redirect('/Patient-profile.html')
        except:
            return "There was an error adding new patient"

    else:
        return render_template('/Patient-registration.html')


if __name__ == "__main__":
    app.run()
