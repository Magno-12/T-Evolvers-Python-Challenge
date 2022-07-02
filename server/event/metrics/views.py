from ast import Not
import json
import re
from flask import request, jsonify, Blueprint, abort, make_response
from flask.views import MethodView
from event import db, app, api
from event.metrics.models import Metrics
from flask_restful import Resource, reqparse

catalog = Blueprint('catalog', __name__)

parser = reqparse.RequestParser()
parser.add_argument('device_id', type=str)
parser.add_argument('metrics', type=str)
parser.add_argument('timestamp', type=int)


@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Metrics Home."


class MetricApi(Resource):
    def get(self, id=None, page=1):
        try:
            res = {}

            if not id:
                metrics = Metrics.query.all()
            else:
                metrics = [Metrics.query.get(id)]
            if not metrics:
                res['code'] = "204"
            else:
                result = []
                for metric in metrics:
                    result.append({
                        'id': metric.id,
                        'device_id': metric.device_id,
                        'metric': metric.metrics,
                        'timestamp': metric.timestamp,
                    })

            res["data"] = result
            res["code"] = 200
            return res
        except:
            abort(500)

    def post(self):

        args = parser.parse_args()
        device_id = args['device_id']
        metrics = args['metrics']
        timestamp = args['timestamp']

        event = Metrics(device_id, metrics, timestamp)
        print(event)
        db.session.add(event)
        db.session.commit()

        return {
            'event_id': event.id,
            'metrics': event.metrics,
            'device_id': event.device_id,
        }

    def put(self, id=None):

        args = parser.parse_args()
        print(args['metrics'] is None)

        if args['metrics'] is None and args['device_id'] is None and args['timestamp'] is None:
            return make_response("Remember to send parameters to update", 400)

        if id is None:
            return make_response("You must send the id", 400)

        get_metric = Metrics.query.get(id)

        if not get_metric:
            return make_response("This object not exist", 400)

        if args['device_id'] is not None:
            get_metric.device_id = args['device_id']

        if args['metrics'] is not None:
            get_metric.metrics = args['metrics']

        if args['timestamp'] is not None:
            get_metric.timestamp = args['timestamp']

        db.session.commit()

        return make_response("", 200)

    def delete(self, id=None):
        get_metric = Metrics.query.get(id)
        db.session.delete(get_metric)
        db.session.commit()

        return make_response("", 200)


api.add_resource(
    MetricApi,
    '/api/metric',
    '/api/metric/<int:id>',
    '/api/metric/<int:id>/<int:page>'
)
