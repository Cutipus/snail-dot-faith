import time
from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html", title="Snail Church", heading="Roll the Dice")


@app.route("/update")
def update() -> str:
    dicenum: int = randint(1, 6)
    rand: str = str(time.time())
    if "Firefox" in str(request.user_agent):
        # see https://bugzilla.mozilla.org/show_bug.cgi?id=129986
        return render_template("dice-firefox.html", dice_num=str(dicenum), rand=rand)
    else:
        return render_template("dice.html", dice_num=str(dicenum))
