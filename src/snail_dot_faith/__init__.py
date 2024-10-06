from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    return render_template("index.html", title="Snail Church", heading="Regular")


@app.route("/update")
def update() -> str:
    return render_template("button_response.html", randnum=str(randint(0, 100)))
