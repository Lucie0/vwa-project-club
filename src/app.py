import os

from flask import Flask

# initialize application
app = Flask(__name__)

# app configuration
environ = os.environ.get("FLASK_ENV")
if environ == "production":
    app.config.from_object("src.config.ProductionConfig")
else:
    app.config.from_object("src.config.DevelopmentConfig")

if __name__ == "__main__":
    app.run()
