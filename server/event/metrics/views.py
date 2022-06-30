import json
from flask import request, jsonify, Blueprint, abort
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
                metrics = Metrics.query.paginate(page, 10).items
            else:
                metrics = [Metrics.query.get(id)]
            if not metrics:
                res['code'] = "204"

            for metric in metrics:
                res[metric.id] = {
                    'device_id': metric.device_id,
                    'metric': metric.metric,
                    'timestamp': metric.timestamp,
                }
            if not metrics:
                return res
            else:
                return json.dumps(res)
        except:
            abort(500)

    def post(self):

        args = parser.parse_args()
        device_id = args['device_id']
        metrics = args['metrics']
        timestamp = args['timestamp']

        event = Metrics(device_id, metrics, timestamp)
        db.session.add(event)
        db.session.commit()

        res = {}
        res[event.id] = {
            'metrics': event.metrics,
            'device_id': event.device_id,
        }
        return json.dumps(res)


api.add_resource(
    MetricApi,
    '/api/metric',
    '/api/metric/<int:id>',
    '/api/metric/<int:id>/<int:page>'
)
