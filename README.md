# Hemodialysis Department
## Team 17
### Team Members
Name| Section | Bench Number |
--- | --- | --- |
Rawan Abdulhamid Ali | 1 | 34
Sohaila Mahmoud Hussein | 1 | 46
Shrouk Shawky Elsayed | 1 | 47
Omar Mustafa | 2 | 5
Mina Azer | 2 | 45
Yehia Said | 2 | 54
___
## ER Model
![ER Diagram](ER%20Model.png)

## Usage
Open the project on any IDE that uses Flask Python. To install Flask, run the following command:

```
pip install flask
```

Now follow the following steps to ensure the program runs correctly on your IDE:
1. First, run ***database-create.py*** to create MySQL database on your computer. (*Note: Change the MySQL host password to your own*)
2. Run ***database.py*** to create the tables in the above MySQL database. (*Note: Do the same by changing the host password to your own*)
3. Now run ***server.py*** and the website should work with you on any web browser. (*Note: Do the same by changing the host password to your own*)

## Project constituents
The project is made using Flask Python (Back-end) and the following Front-end languages:
- HTML
- CSS
- JavaScript
- PHP

The website contains the main page from which you can get more information about hemodialysis, and navigate to other pages.
From the main page you can go to the registration pages (*admin, doctor, and patient registration pages*), login page that leads you to your respective profile (*whether it's admin, doctor, or patient profile*), and view page that shows you all the information in the database (***except admins password***)