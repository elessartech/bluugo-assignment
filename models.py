from db import db
from sqlalchemy import Index, func, cast
from sqlalchemy.dialects import postgresql

def create_tsvector(*args):
    colummns = args[0]
    for column in args[1:]:
        colummns += ' ' + column
    return func.to_tsvector('english', colummns)

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    model_year = db.Column(db.Integer, nullable=False)
    make = db.Column(db.Text, nullable=False)
    model = db.Column(db.Text, nullable=False)
    rejection_percentage = db.Column(db.Float, nullable=False)
    reason_1 = db.Column(db.Text, nullable=True)
    reason_2 = db.Column(db.Text, nullable=True)
    reason_3 = db.Column(db.Text, nullable=True)
    __ts_vector__ = create_tsvector(
        cast(func.to_tsvector('english', make + " " + model + " " + reason_1 + " " + reason_2 + " " + reason_3), postgresql.TEXT)
    )
    __table_args__ = (
        Index(
            'ix_vehicle_fts',
            func.to_tsvector('english', make + " " + model + " " + reason_1 + " " + reason_2 + " " + reason_3),
            postgresql_using='gin'
        ),
    )