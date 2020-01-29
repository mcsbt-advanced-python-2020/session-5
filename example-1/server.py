from flask import Flask, render_template, request

app = Flask(__name__)

users = {
    "admin": "admin",
    "pepe": "p4ssw0rd"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/handle", methods = ["POST"])
def handle_form_submission():
    user = request.form["user"]
    password = request.form["pass"]

    if user in users and users[user] == password:
        return "logged in!"
    else:
        return "not logged in..."

app.run(debug = True)
