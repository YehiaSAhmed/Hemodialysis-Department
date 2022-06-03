import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="leviosa",
  database="Hemodialysis"
)

mycursor = mydb.cursor()


mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x) 

