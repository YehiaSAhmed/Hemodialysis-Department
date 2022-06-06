import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="erer@100@",
  database="Hemodialysis"
)

mycursor = mydb.cursor()


mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x) 

mycursor.execute("SHOW COLUMNS FROM admin")
for x in mycursor:
  print(x) 

mycursor.execute("SHOW COLUMNS FROM care")
for x in mycursor:
  print(x) 

mycursor.execute("SHOW COLUMNS FROM doctor")
for x in mycursor:
  print(x) 

mycursor.execute("SHOW COLUMNS FROM medical_history")
for x in mycursor:
  print(x) 

mycursor.execute("SHOW COLUMNS FROM nurse")
for x in mycursor:
  print(x) 

mycursor.execute("SHOW COLUMNS FROM patient")
for x in mycursor:
  print(x) 

mycursor.execute("SHOW COLUMNS FROM prescribe")
for x in mycursor:
  print(x) 

mycursor.execute("SHOW COLUMNS FROM prescription")
for x in mycursor:
  print(x) 

mycursor.execute("SHOW COLUMNS FROM treat")
for x in mycursor:
  print(x) 
