from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Connect to SQLite database
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Create employees table if it does not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        department TEXT NOT NULL,
        position TEXT NOT NULL
    )
''')
conn.commit()

# Close the cursor and the database connection
cursor.close()
conn.close()

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

        # Connect to SQLite database
        conn = sqlite3.connect('employees.db')
        cursor = conn.cursor()

        # Insert the employee data into the database
        cursor.execute('''
            INSERT INTO employees (name, email, department, position)
            VALUES (?, ?, ?, ?)
        ''', (name, email, department, position))
        conn.commit()

        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        return redirect(url_for('information'))

    return render_template('registration.html')

# Employee information page
@app.route('/information')
def information():
    # Connect to SQLite database
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    # Get all employees' information from the database
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

    return render_template('information.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
