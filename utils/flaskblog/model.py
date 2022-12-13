from flask_login import UserMixin
from .. import db, login_manager
import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def getlastdate(anyDay):
    next_month = anyDay.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)

class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    memberships = db.relationship('Membership', lazy=True, uselist=False, backref='User')
    
    def __repr__(self) -> str:
        return f"User: ('{self.username}', '{self.email}', '{self.age}')"

class Batch(db.Model):

    batchId = db.Column(db.Integer, nullable=False, primary_key=True)
    batchTime = db.Column(db.String(10), nullable=False)

    memberships = db.relationship("Membership", lazy=True, backref="Members")

    def __repr__(self) -> str:
        return f"Batch: ('{self.batchId}', '{self.batchTime}')"

class Membership(db.Model):
    
    memId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    batchId = db.Column(db.Integer, db.ForeignKey('batch.batchId'), nullable=False)
    datePaid = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now().date())
    dateValid = db.Column(db.DateTime, nullable=False, default=getlastdate(datetime.datetime.now().date()))
    status = db.Column(db.Boolean, nullable=False)

    def __repr__(self) :
        return f"Membership: ('{self.userId}', '{self.datePaid}', '{self.dateValid}', '{self.status}')"



def init_db():
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    init_db()
