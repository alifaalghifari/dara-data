from flask import Flask
from flask_cors import CORS
from flask_compress import Compress
# from configuration import Configuration
import routes
from datetime import date


# import app
# from flask_mysqldb import MySQL
# from helpers.connecttion import mysql

cors = CORS()
compress = Compress()

import os


def create_app(configuration):
    app = Flask(__name__.split(',')[0], template_folder='../templates', static_folder='../static')
    # print(configuration)

    # register route blueprint
    app.register_blueprint(routes.OlahDataRoute.bp)
    app.register_blueprint(routes.PemodelanRoute.bp)
    app.register_blueprint(routes.VisualisasiRoute.bp)

    # load configuration
    app.config.from_object(configuration)

    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    compress.init_app(app)

   
    return app

