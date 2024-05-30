from flask import render_template

from app_file import app

from pages import (
    analytics,
)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("home.html")


if __name__=="__main__":
    app.run(debug=True)
