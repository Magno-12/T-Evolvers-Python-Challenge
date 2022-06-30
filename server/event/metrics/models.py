from event import db

class Metrics(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    device_id=db.Column(db.String(255),nullable=False,unique=True)
    metrics=db.Column(db.Text)
    timestamp=db.Column(db.Integer,nullable=False)

    def __init__(self, device_id, metrics, timestamp):
        self.device_id = device_id
        self.metrics = metrics
        self.timestamp = timestamp

    def __repr__(self):
        return f"<Event device_id={self.device_id} metrics={self.metrics}>"