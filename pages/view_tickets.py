from flask import  render_template, request, session

from apps.ticket import create_ticket
from app_file import app

@app.route('/view_tickets', methods=['GET', 'POST'])
def view_tickets():
    ticket = create_ticket(
        session["ticket_inputs"]["ticket_description"],
        session["ticket_inputs"]["ticket_detail"],
        session["ticket_inputs"]["tools"],
        session["ticket_inputs"]["features"],
    )

    return render_template("view_tickets.html")
