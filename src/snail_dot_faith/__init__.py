from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html", title="Snail Church", heading="Roll the Dice")


@app.route("/whoami")
def who_am_i() -> str:
    return render_template("about-me.html", title="About Me", heading="Cutipus")
