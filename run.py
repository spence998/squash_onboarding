from flask import render_template, request, redirect, session, url_for
from app_file import app

from pages import (
    view_tickets,
)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session['ticket_inputs'] = {
            "ticket_description": request.form["ticket_description"],
            "ticket_detail": request.form["ticket_detail"],
            "tools": request.form["tools"],
            "features": request.form["features"],
        }
        return redirect(url_for('view_tickets'))
    else:
        return render_template("home.html")


if __name__=="__main__":
    app.run(debug=True)
