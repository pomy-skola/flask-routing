from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    today = datetime.now()
    return render_template("index.html", today=today)


@app.route("/o-mne")
def about_me():
    return render_template("o-mne.html")
