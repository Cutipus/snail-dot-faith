from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    return render_template("index.html", title="snail.faith", heading="Home")


@app.route("/update")
def update() -> str:
    return f"<p><3 i love snails 🐌  (and here's your random number: {randint(0, 100)})</p>"
