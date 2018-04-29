from flask import Flask, render_template, session, redirect, flash, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'A3$lkq90!!%2'
mysql = MySQLConnector(db, 'name_DB')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validation', methods=['POST'])
def validate():
    return redirect('/')

app.run(debug=True)
