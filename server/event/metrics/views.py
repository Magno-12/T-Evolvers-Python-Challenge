import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from event import db, app,api
from event.metrics.models import Metrics
from flask_restful import Resource,reqparse

catalog = Blueprint('catalog', __name__)

parser = reqparse.RequestParser()
parser.add_argument('device_id', type=str)
parser.add_argument('metrics', type=str)
parser.add_argument('timestamp', type=int)

@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."