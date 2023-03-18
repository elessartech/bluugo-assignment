from db import db


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_year = db.Column(db.Integer, nullable=False)
    make = db.Column(db.Text, nullable=False)
    model = db.Column(db.Text, nullable=False)
    rejection_percentage = db.Column(db.Float, nullable=False)
    reason_1 = db.Column(db.Text, nullable=True)
    reason_2 = db.Column(db.Text, nullable=True)
    reason_3 = db.Column(db.Text, nullable=True)
