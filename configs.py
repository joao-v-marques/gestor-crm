from controllers.routes.bp_home import bp_home
from controllers.routes.bp_login import bp_login

def config_all(app):
    config_bp(app)

def config_bp(app):
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_login)