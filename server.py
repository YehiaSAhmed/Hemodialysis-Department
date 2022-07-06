from flask import Flask
from flask import render_template, request, redirect, url_for
from email.policy import default
from datetime import datetime
import os
import sys
from sympy import Id
import mysql.connector
from flask import Flask, redirect, url_for, request, render_template

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="root",
      database="HemodialysisProject"
)
mycursor = mydb.cursor()
app = Flask(__name__)


STATIC_FOLDER = 'assets'
app = Flask(__name__, static_folder=STATIC_FOLDER)

STATIC_FOLDER_2 = 'static'
app = Flask(__name__, static_folder=STATIC_FOLDER)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/View.html/index.html')
def home():
    return render_template('index.html')

@app.route('/Login.html/index.html')
def Lhome():
    return render_template('index.html')


@app.route('/View.html/')
def view():
    mycursor.execute("SELECT * FROM admin")
    adminresult = mycursor.fetchall()

    mycursor.execute("SELECT * FROM doctor")
    doctorresult = mycursor.fetchall()

    mycursor.execute("SELECT * FROM patient")
    patientresult = mycursor.fetchall()

    return render_template('view.html', a=adminresult, d=doctorresult, p=patientresult)


d_ide = ''
a_ide = ''
p_ide = ''



@app.route('/Login.html/', methods=["POST", "GET"])
def Login():
    if request.method == "POST":
            ide = request.form['id']
            password = request.form['password']
            if (request.form['flexRadioDefault'] == "doctor"):
                d_ide = request.form['id']
                sql = "SELECT * FROM doctor WHERE D_id = %s"
                val = ide
                mycursor.execute(sql, (val,))
                myresult = mycursor.fetchall()
                return redirect(url_for("DoctorProfile"))
            elif (request.form['flexRadioDefault'] == "admin"):
                a_ide = request.form['id']
                sql = "SELECT * FROM admin WHERE A_id = %s"
                val = ide
                mycursor.execute(sql, (val,))
                myresult = mycursor.fetchall()
                return redirect(url_for("AdminProfile"))
            elif (request.form['flexRadioDefault'] == "patient"):
                p_ide = request.form['id']
                sql = "SELECT * FROM patient WHERE P_id = %s"
                val = ide
                mycursor.execute(sql, (val,))
                myresult = mycursor.fetchall()
                return redirect(url_for("PatientProfile"))
    else:
        return render_template('/Login.html')


@app.route('/Admin-profile.html')
def AdminProfile():
    ide = a_ide
    sql = "SELECT * FROM admin WHERE A_id = %s"
    val = ide
    mycursor.execute(sql, (val,))
    info = mycursor.fetchall()
    return render_template('/Admin-profile.html', msg = info)
    

@app.route('/Doctor-profile.html')
def DoctorProfile():
    ide = d_ide
    sql = "SELECT * FROM admin WHERE A_id = %s"
    val = ide
    mycursor.execute(sql, (val,))
    info = mycursor.fetchall()
    return render_template('/Doctor-profile.html', msg = info)


@app.route('/Patient-profile.html')
def PatientProfile():
    ide = p_ide
    sql = "SELECT * FROM admin WHERE A_id = %s"
    val = ide
    mycursor.execute(sql, (val,))
    info = mycursor.fetchall()
    return render_template('/Patient-profile.html', msg = info)


@app.route('/Admin-registration.html/', methods=["POST", "GET"])
def AdminRegistration():
    title = "Our Admins list"

    if request.method == "POST":
        A_fname = request.form['A_fname']
        A_mname = request.form['A_mname']
        A_lname = request.form['A_lname']
        A_gender = request.form['A_gender']
        A_ssn = request.form['A_ssn']
        A_address = request.form['A_address']
        A_ID = request.form['A_ID']
        A_Email = request.form['A_email']
        A_Phone = request.form['A_phone']
        A_bd = request.form['A_bd']
        A_Password = request.form['A_password']
        A_c_Password = request.form['A_cpassword']
        if A_Password == A_c_Password:
                sql = "INSERT INTO admin (A_id, A_fname, A_mname, A_lname, A_email, A_phone, A_password, A_gender, A_ssn, A_address, A_bd) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (A_ID,A_fname, A_mname, A_lname, A_Email, A_Phone, A_Password, A_gender, A_ssn, A_address,A_bd)
                mycursor.execute(sql, val)
                mydb.commit()
                return render_template('Login.html', message="Welcome Admin " + A_fname)

                # return render_template('Admin-profile.html', error="Something Went wrong ")
        else:
            # return render_template('/Admin-registration.html', error="password and cofirmed password must be equal")
            return render_template('Admin-registration.html')
    else:
        return render_template('/Admin-registration.html')


@app.route('/Doctor-registration.html/', methods=["POST", "GET"])
def DoctorRegistration():
    title = "Our Doctors list"

    if request.method == "POST":
        D_fname = request.form['D_fname']
        D_mname = request.form['D_mname']
        D_lname = request.form['D_lname']
        D_gender = request.form['D_gender']
        D_ssn = request.form['D_ssn']
        D_address = request.form['D_address']
        D_ID = request.form['D_ID']
        D_Email = request.form['D_email']
        D_Phone = request.form['D_phone']
        D_bd = request.form['D_bd']
        D_Password = request.form['D_password']
        D_c_Password = request.form['D_cpassword']
        if D_Password == D_c_Password:
                sql = "INSERT INTO doctor (D_id, D_fname, D_mname, D_lname, D_email, D_phone, D_password, D_gender, D_ssn, D_address, D_bd) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (D_ID, D_fname, D_mname, D_lname, D_Email, D_Phone, D_Password, D_gender, D_ssn, D_address, D_bd)
                mycursor.execute(sql, val)
                mydb.commit()
                return render_template('Login.html', message="Welcome Admin " + D_fname)
        else:
            return render_template('/Doctor-registration.html', error="password and cofirmed password must be equal")
    else:
        return render_template('/Doctor-registration.html')


@app.route('/Patient-registration.html/', methods=['POST', 'GET'])
def PatientRegistration():
    title = "Our Patients list"

    if request.method == "POST":
        P_fname = request.form['P_fname']
        P_mname = request.form['P_mname']
        P_lname = request.form['P_lname']
        P_ID = request.form['P_id']
        P_Email = request.form['P_email']
        P_Phone = request.form['P_phone']
        P_Gender = request.form['P_gender']
        P_BloodType = request.form['bloodtype']
        P_bd = request.form['P_bd']
        P_Password = request.form['P_password']
        p_c_password = request.form['P_cpassword']
        P_ssn = request.form['P_ssn']
        P_address = request.form['P_address']

        if P_Password == p_c_password:
            
                ##new_patient = mydb.patient(P_id=P_ID, P_ssn=P_SSN, P_fname=P_name, P_email=P_Email, P_phone=P_Phone, P_gender=P_Gender,
                                           ##medicalstat=P_TreatingDoctor, bloodtype=P_BloodType, P_bd=P_DateOfBirth, _password=P_Password)
                sql = "INSERT INTO patient (P_id, P_fname, P_mname, P_lname, P_email, P_Phone, P_gender, bloodtype, P_bd, P_password, P_ssn, P_address) VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (P_ID, P_fname, P_mname, P_lname, P_Email, P_Phone, P_Gender, P_BloodType, P_bd, P_Password, P_ssn, P_address)
                mycursor.execute(sql, val)
                mydb.commit()
                return render_template('Login.html', message="Welcome patient " + P_fname)
        else:
            return render_template('/Patient-registration.html', massage="password and cofirmed password must be equal")
    else:
        return render_template('/Patient-registration.html')


if __name__ == "__main__":
    app.run()
