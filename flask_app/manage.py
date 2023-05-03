from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Connect to MySQL database
db = sql.connect(
    host="localhost",
    user="flask",
    password="ubuntu",
    database="flask_db"
)

# Create employees table if it does not exist
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        department VARCHAR(255) NOT NULL,
        position VARCHAR(255) NOT NULL
    )
''')
db.commit()

# Close the cursor and the database connection
cursor.close()
db.close()

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Employee registration page
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']
        position = request.form['position']

        # Connect to MySQL database
        db = sql.connect(
            host="localhost",
            user="your-username",
            password="your-password",
            database="employees_db"
        )
        cursor = db.cursor()

        # Insert the employee data into the database
        cursor.execute('''
            INSERT INTO employees (name, email, department, position)
            VALUES (%s, %s, %s, %s)
        ''', (name, email, department, position))
        db.commit()

        # Close the cursor and the database connection
        cursor.close()
        db.close()

        return redirect(url_for('information'))

    return render_template('registration.html')

# Employee information page
@app.route('/information')
def information():
    # Connect to MySQL database
    db = sql.connect(
        host="localhost",
        user="your-username",
        password="your-password",
        database="employees_db"
    )
    cursor = db.cursor()

    # Get all employees' information from the database
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    db.close()

    return render_template('information.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
