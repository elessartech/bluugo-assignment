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

def save_rejection(model_year, make, model, rejection_percentage, reason_1, reason_2, reason_3):
    rejection = Rejections(
        model_year=model_year,
        make=make,
        model=model,
        rejection_percentage=rejection_percentage,
        reason_1=reason_1,
        reason_2=reason_2,
        reason_3=reason_3
    )
    db.session.add(rejection)
    db.session.commit()
    return True

def get_rejections():
    return db.session.execute(db.select(Rejections)).scalars().fetchall()