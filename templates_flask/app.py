from flask import render_template
from flask import Flask

import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "HARRY_POTTER"
)
mycursor = mydb.cursor()

app = Flask(__name__)


 
@app.route('/units')
def unitlist():
    mycursor.execute("SELECT * FROM character_Unit")
    myresult = mycursor.fetchall()
    return render_template('hello.html', units=myresult)