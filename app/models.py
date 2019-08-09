from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    phone_number = db.Column(db.String(255), index = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'

class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(5))

    def __repr__(self):
        return f'Admin {self.name}'
    
class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer,primary_key = True)
    Quantity = db.Column(db.Integer)
    cost=db.Column(db.Integer)
    Description = db.Column(db.String(255))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    clientID = db.Column(db.Integer, db.ForeignKey('users.id'))
    totalCost = db.Column(db.Integer)
    
    def save_order(self):
        db.session.add(self)
        db.session.commit()
        return orders
    def calculate_total_cost(self,quantity,prize):
        total = Quantity * cost
        return total(self.totalCost)
    
    def __repr__(self):
        return f'Order {self.totalCost}'
    
