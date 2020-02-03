#%%
from flask import Flask, render_template, request

tweets = []

app = Flask(__name__)

@app.route("/")
def show_all_tweets():
    return render_template("index.html", tweets=tweets)

@app.route("/", methods = ["POST"])
def new_tweet():
    username = request.form["username"]
    tweet = request.form["tweet"]
    tweets.append({"username": username, "tweet": tweet})
    return render_template("index.html", tweets=tweets)

app.run(debug = True)