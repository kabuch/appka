import flask
from flask import render_template


app = flask.Flask(__name__)


@app.route("/")
def index():
    tekst = "Hello User"
    # miesiac = datetime.time(datetime.now)
    imiona = "jan", "maria"

    return render_template("index.html", text = tekst, tab = imiona, taba = imiona)


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":  # There is an error on this line
    app.run()
