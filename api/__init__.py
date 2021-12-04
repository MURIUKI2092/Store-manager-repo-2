from flask import Flask,Blueprint,Response,jsonify
from flask_restful import Api,Resource,reqparse

#created a app blueprint and also the api blueprint
app=Flask(__name__)
api=Api(app,prefix='/api')
apiBp=Blueprint('api',__name__)