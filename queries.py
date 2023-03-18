from sqlalchemy import func, or_, and_
from db import db
from models import Vehicle


def save_vehicle(
    model_year, make, model, rejection_percentage, reason_1, reason_2, reason_3
):
    vehicle = Vehicle(
        model_year=model_year,
        make=make,
        model=model,
        rejection_percentage=rejection_percentage,
        reason_1=reason_1,
        reason_2=reason_2,
        reason_3=reason_3,
    )
    db.session.add(vehicle)
    db.session.commit()
    return True


def get_vehicles():
    return db.session.execute(db.select(Vehicle)).scalars().fetchall()


def get_vehicle(model_year, make, model):
    return db.session.execute(
        db.session.query(Vehicle).filter_by(
            model_year=model_year, make=make, model=model
        )
    ).scalar()


def update_vehicle(id, rejection_percentage, reason_1, reason_2, reason_3):
    Vehicle.query.filter_by(id=id).update(
        dict(
            rejection_percentage=rejection_percentage,
            reason_1=reason_1,
            reason_2=reason_2,
            reason_3=reason_3,
        )
    )
    db.session.commit()
    return True


def filter_vehicles(searchbar_val):
    searchbar_splitted = searchbar_val.lower().split(" ")
    if searchbar_splitted[-1] == "":
        searchbar_val = searchbar_val.strip()
    return (
        Vehicle.query.filter(
            or_(
                func.lower(Vehicle.make).ilike(f"%{searchbar_val}%"),
                func.lower(Vehicle.model).ilike(f"%{searchbar_val}%"),
                and_(
                    func.lower(Vehicle.make).in_(searchbar_splitted),
                    func.lower(Vehicle.model).in_(searchbar_splitted),
                ),
            )
        )
        .limit(50)
        .all()
    )
