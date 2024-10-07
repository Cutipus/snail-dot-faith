import time
from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html", title="Snail Church", heading="Roll the Dice")


@app.route("/update")
def update() -> str:
    dicenum: int = randint(1, 6)
    rand: str = str(time.time())
    return render_template("dice.html", dice_num=str(dicenum), rand=rand)


@app.route("/whoami")
def who_am_i() -> str:
    return render_template("about-me.html", title="About Me", heading="Cutipus")
