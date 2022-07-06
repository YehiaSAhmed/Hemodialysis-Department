import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="HemodialysisProject"
)

mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE admin (A_fname VARCHAR(255), A_mname VARCHAR(255), A_lname VARCHAR(255), A_id VARCHAR(255), A_gender VARCHAR(255), A_ssn VARCHAR(255), A_address VARCHAR(255), A_bd VARCHAR(255), A_phone VARCHAR(255), A_email VARCHAR(255), A_password VARCHAR(255))")

mycursor.execute("CREATE TABLE doctor (D_fname VARCHAR(255), D_mname VARCHAR(255), D_lname VARCHAR(255), D_id VARCHAR(255), D_gender VARCHAR(255), D_ssn VARCHAR(255), D_address VARCHAR(255), D_password VARCHAR(255), D_bd VARCHAR(255), D_phone VARCHAR(255), D_email VARCHAR(255))")

mycursor.execute("CREATE TABLE patient (P_fname VARCHAR(255), P_mname VARCHAR(255), P_lname VARCHAR(255), P_id VARCHAR(255), P_ssn VARCHAR(255), P_address VARCHAR(255), P_password VARCHAR(255), P_bd VARCHAR(255), P_gender VARCHAR(255), bloodtype VARCHAR(255), P_Phone VARCHAR(255), P_email VARCHAR(255))")