from flask import Flask, Response, request
from flask_restful import Resource
from guildroom import read_serialport, utils, api
from guildroom import utils, api # db, models

ser = read_serialport.SerialReader()    # Initializing serialreader to read data from arduino

class Guildroom(Resource):

    def get(self):
        if request.method != "GET":
            return utils.RecipeBuilder.create_error_response(405, "wrong method", "GET method required")
