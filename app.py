from flask import Flask, render_template, url_for, redirect, request, session, flash, g
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os

app = Flask(__name__)
Bootstrap(app)


app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'       
app.config['MYSQL_PASSWORD'] = ''       
app.config['MYSQL_DB'] = 'restaurant'  
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
    session.pop('user', None)
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.pop('user', None)
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user and user['password'] == password:  # Ensure column name matches DB
            session['user'] = email
            return redirect(url_for('protected'))
        else:
            flash('Invalid credentials, try again.', 'danger')
            return render_template('login.html')

    return render_template('login.html')
@app.route('/loginDoc', methods=['POST', 'GET'])
def loginDoc():
    if request.method == 'POST':
        session.pop('user', None)
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user and user['password'] == password:  # Ensure column name matches DB
            session['user'] = email
            return redirect(url_for('dashboard2'))
        else:
            flash('Invalid credentials, try again.', 'danger')
            return render_template('loginDoc.html')

    return render_template('loginDoc.html')
@app.route('/protected')
def protected():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    return redirect(url_for('login'))
@app.route('/dashboard2')
def dashboard2():
    print(session)  # Debugging: Check session storage
    if 'user' in session:
        return render_template('dashboard2.html', user=session['user'])
    return redirect(url_for('loginDoc'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        userDetails = request.form
        if userDetails['password'] != userDetails['confirm_password']:
            flash('Passwords do not match! Try again.', 'danger')
            return render_template('signup.html')

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (location, name, username, password) VALUES (%s, %s, %s, %s)", 
                    (userDetails['location'], userDetails['first_name'], userDetails['email'], userDetails['password']))
        mysql.connection.commit()
        cur.close()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

# @app.route('/loginDoc')
# def loginDoc():
#     return render_template('loginDoc.html')

@app.route("/add")
def add():
    if 'user' in session:
        return render_template('add.html')
    return redirect(url_for('login'))

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.urandom(24)

# Ensure upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/uploadP", methods=['GET', 'POST'])
def uploadP():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            flash('File successfully uploaded', 'success')
            return render_template('uploadp.html', filename=file.filename)

    return render_template('uploadp.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
# -------- Search Doctors/Hospitals Route --------
@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')
@app.route('/patient_history', methods=['GET'])
def patient_history():
    return render_template('patient_history.html')
if __name__ == '__main__':
    app.run(debug=True, port=5001)
