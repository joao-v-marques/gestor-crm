import logging
from flask import Blueprint, render_template, jsonify
from models.connect_db import conectar_db, dict_fetchall

bp_home = Blueprint("bp_home", __name__)

@bp_home.route("/home")
def pagina():
    return render_template("home.html")

@bp_home.route("/home/api")
def teste_db():
    try:
        conn = conectar_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM test_table ORDER BY ID")
        data = dict_fetchall(cursor)

        return data
    except Exception as e:
        logging.error(f"Houve um erro na API: {e}")
        return jsonify({"erro": f"{e}"}), 500
    finally:
        cursor.close()
        conn.close()