from flask import Blueprint, render_template

bp_login = Blueprint("bp_login", __name__)

@bp_login.route("/")
def pagina():
    return render_template("login.html")