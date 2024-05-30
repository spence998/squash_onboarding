from flask import render_template

from app_file import app
 

@app.route('/analytics', methods=['GET'])
def analytics():
    return render_template("analytics.html")
