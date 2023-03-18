from sqlalchemy import func, or_, and_
from db import db


class Rejections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_year = db.Column(db.Integer, nullable=False)
    make = db.Column(db.Text, nullable=False)
    model = db.Column(db.Text, nullable=False)
    rejection_percentage = db.Column(db.Float, nullable=False)
    reason_1 = db.Column(db.Text, nullable=True)
    reason_2 = db.Column(db.Text, nullable=True)
    reason_3 = db.Column(db.Text, nullable=True)


def save_rejection(
    model_year, make, model, rejection_percentage, reason_1, reason_2, reason_3
):
    rejection = Rejections(
        model_year=model_year,
        make=make,
        model=model,
        rejection_percentage=rejection_percentage,
        reason_1=reason_1,
        reason_2=reason_2,
        reason_3=reason_3,
    )
    db.session.add(rejection)
    db.session.commit()
    return True


def get_rejections():
    return db.session.execute(db.select(Rejections)).scalars().fetchall()


def filter_rejections(searchbar_val):
    searchbar_splitted = searchbar_val.split(" ")
    if (searchbar_splitted[-1] == ''):
        searchbar_val = searchbar_val.strip()
    return Rejections.query.filter(
        or_(
            func.lower(Rejections.make).ilike(f"%{searchbar_val}%"),
            func.lower(Rejections.model).ilike(f"%{searchbar_val}%"),
            and_(
                func.lower(Rejections.make).in_(searchbar_splitted),
                func.lower(Rejections.model).in_(searchbar_splitted),
            )
    )).all() 

