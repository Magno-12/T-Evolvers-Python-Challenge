import os
import pika
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['TASK_QUEUE'] = 'task_queue'
app.config['PYTHONUNBUFFERED'] = '1'
app.config['RABBITMQ_USER'] = 'rabbitmq'
app.config['RABBITMQ_PORT'] = '5672'

def wait_for_queue_connection():
    while True:
        try:
            params = pika.ConnectionParameters(host='localhost')
            connection = pika.BlockingConnection(params)
            break
        except Exception as ex:
            print("Producer not connected to queue yet..")
            time.sleep(1)
    print("Connected")
    return connection

from event.metrics.views import catalog
app.register_blueprint(catalog)

connection = wait_for_queue_connection()
channel = connection.channel()
channel.queue_declare(queue=app.config['TASK_QUEUE'])
channel.basic_qos(prefetch_count=1)

db.create_all()