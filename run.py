from flask import render_template, request, redirect, session, url_for
from app_file import app

from pages import (
    view_tickets,
)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        session['ticket_inputs'] = {
            "ticket_description": request.form.get(f'ticket_description', 'N/A'),
            "ticket_detail": request.form.get(f'ticket_detail', 'N/A'),
            "tools": request.form.get(f'tools', 'N/A'),
            "features": request.form.get(f'features', 'N/A'),
        }
        return redirect(url_for('view_tickets'))
    else:
        return render_template("home.html")


if __name__=="__main__":
    app.run()
