from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'foo'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route("/render")
def render():
	return render_template('forms.html')


@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.method == 'GET':
		return "Login via the login Form"

	if request.method == 'POST':
		name = reques.form['name']
		age = rquest.form['age']
		cursor = mysql.connection.cursor()
		cursor.execute(''' INSERT INTO info_table VALUES (%s,%s)''',(name,age))
		mysql.connection.commit()
		cursor.close()
		return f"Done!!"
