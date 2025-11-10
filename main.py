from flask import Flask
from configs import config_all

app = Flask(
    __name__,
    template_folder="views/templates",
    static_folder="views/static"
    )

config_all(app)

app.run(debug=True)