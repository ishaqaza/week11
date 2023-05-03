from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap

import mysql.connector as sql

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_employee():
   return render_template('registration.html')


@app.route('/addrec', methods=['POST'])
def addrec():
   try:
      name = request.form['name']
      gender = request.form['gender']
      phone = request.form['phone']
      bdate = request.form['bdate']
      
      with sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db") as con:
         cur = con.cursor()
         cmd = "INSERT INTO Employee (EmpName, EmpGender, EmpPhone, EmpBDate) VALUES (%s, %s, %s, %s)"
         cur.execute(cmd, (name, gender, phone, bdate))
         
         con.commit()
         msg = "Record successfully added"
   except:
      con.rollback()
      msg = "Error in insert operation"
   finally:
      con.close()
      return render_template("output.html", msg=msg)


@app.route('/list')
def list_employees():
   with sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db") as conn:  
      cur = conn.cursor()
      cur.execute("SELECT * FROM Employee")
      rows = cur.fetchall()

   return render_template("information.html", rows=rows)

if __name__ == '__main__':
   app.run() 
