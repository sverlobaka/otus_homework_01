from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate
from models import db

import config

from views.views import books_app

app = Flask(__name__)
app.register_blueprint(books_app)

CONFIG_NAME = getenv("CONFIG_NAME", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_NAME}")

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/", endpoint="index")
def root():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)