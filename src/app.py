import os

from flask import Flask
from src.routes.api import api_blueprint
from src.routes.web import web_blueprint, admin_blueprint, err_blueprint

# initialize application
app = Flask(__name__)

# app configuration
environ = os.environ.get("FLASK_ENV")
if environ == "production":
    app.config.from_object("src.config.ProductionConfig")
else:
    app.config.from_object("src.config.DevelopmentConfig")

# register blueprints
app.register_blueprint(api_blueprint)
app.register_blueprint(web_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(err_blueprint)

if __name__ == "__main__":
    app.run()
