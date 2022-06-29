from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Integer,Column,Text


class Event(Base):
    __tablename__='event'
    id=Column(Integer,primary_key=True)
    device_id=Column(String(255),nullable=False,unique=True)
    metrics=Column(Text)
    timestamp=Column(Integer,nullable=False)

    def __repr__(self):
        return f"<Event device_id={self.device_id} metrics={self.metrics}>"