from flask import Flask, render_template, request, redirect, url_for, session, flash, abort, Response
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/show/<content>")
def content(content):
    return content

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == "POST":
        tekst = request.form["tekst"]
        print(tekst)
    return redirect(url_for("home"))

@app.route("/title/<tekst>")
def title(tekst):
    return render_template("title.html",title= tekst)

@app.route("/table")
def table():
    table = [[1,3,2],[5,5,7],[1,10,0]]
    return render_template("table.html",table = table)
if __name__ == "__main__":

    app.run(debug=True,host='0.0.0.0', port=5000)