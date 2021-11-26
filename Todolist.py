#importing necessary modules
from flask import * 
#importing sqlite database
import sqlite3
import sqlite3 as sql
import random

id = 0
uid = 0
#starting flask app
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#database connection
conn = sqlite3.connect('todo.db')
conn.execute('CREATE TABLE IF NOT EXISTS TODO (id INTEGER PRIMARY KEY AUTOINCREMENT, tasks TEXT)')

@app.route('/')   
def home():  
    return render_template("Landingpage.html")

@app.route('/addtodo',methods = ['POST', 'GET'] )
def addtodo():
    if request.method == 'POST':
        global id
        id +=1
        tasks = request.form['task']
        with sql.connect("todo.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO TODO (id,tasks) VALUES (?,?)",(id,tasks) )
            con.commit()
            
            flash("Task added successfully")
            
        return redirect("showtasks")
            

@app.route('/showtasks')
def showtasks():
    con = sql.connect("todo.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from TODO")
    rows = cur.fetchall(); 
    return render_template("Landingpage.html",rows = rows)

if __name__ =='__main__':  
    app.run(debug = True)