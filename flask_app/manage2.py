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


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         gender = request.form['gender']
         phone = request.form['phone']
         bdate = request.form['bdate']
         
         with sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO Employee (EmpName, EmpGender, EmpPhone, EmpBDate) VALUES ('{0}', '{1}', '{2}', '{3}')".format(name, gender, phone, bdate)
            cur.execute(cmd)
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
         
      finally:
         return render_template("output.html", msg=msg)
         con.close()

@app.route('/list')
def list():
   with sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db") as conn:  
      cur = conn.cursor()
      cur.execute("SELECT * FROM Employee")
      rows = cur.fetchall()

   return render_template("information.html", rows=rows)

if __name__ == '__main__':
   app.run(debug=True)
