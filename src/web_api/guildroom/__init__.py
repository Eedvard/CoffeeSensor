import os
from flask import Flask

#from flask_sqlalchemy import SQLAlchemy    # Lines 4,5 and 31-34 commented out because db is not currently needed
#db = SQLAlchemy()
from . import api


# Based on http://flask.pocoo.org/docs/1.0/tutorial/factory/#the-application-factory
# Modified to use Flask SQLAlchemy


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, static_folder="static")
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(app.instance_path, "development.db"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    app.register_blueprint(api.api_bp)
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #db.init_app(app)

    #from . import models
    #app.cli.add_command(models.init_db_command)

    return app