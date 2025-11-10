from flask import Flask
from configs import config_all
from models.connect_db import conectar_db

# Inicia o Flask e define a pasta views como templates e static
app = Flask(
    __name__,
    template_folder="views/templates",
    static_folder="views/static"
    )

config_all(app)

app.run(debug=True)