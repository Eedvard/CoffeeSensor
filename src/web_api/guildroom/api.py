import configparser
from flask import Flask, Blueprint
from flask_restful import Resource, Api
from guildroom import read_serialport

api_bp = Blueprint("api", __name__, static_folder='static')
api = Api(api_bp)

@api_bp.route("/")
def index():
    return "saatana"

@api_bp.route("/api/")
def api_index():
    return "paska"


