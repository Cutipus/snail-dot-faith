from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    return render_template("index.html", title="snail.faith", heading="Home")


@app.route("/update")
def update() -> str:
    return "<p>Here’s your dynamic update! 🐌</p>"


if __name__ == "__main__":
    app.run(debug=True)
