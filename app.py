from flask import Flask, render_template, request, redirect, url_for, session, flash, abort, Response
import mysql.connector
app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="10.200.14.13",
        user='lab',
        password='lab',
        database="lab"
    )

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/show/<content>")
def content(content):
    return content

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users(name, passord) VALUES (%s,%s)",(name,password))
        conn.commit()
        cursor.close()
        conn.close()
    return redirect(url_for("home"))

@app.route("/title/<tekst>")
def title(tekst):
    return render_template("title.html",title= tekst)

@app.route("/table")
def table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, passord FROM users")
    table = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("table.html",table = table)
if __name__ == "__main__":

    app.run(debug=True,host='0.0.0.0', port=5000)