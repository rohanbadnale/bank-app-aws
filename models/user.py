from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    fullname = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    phone = db.Column(db.String(15), nullable=True)

    address = db.Column(db.String(255), nullable=True)

    account_number = db.Column(db.String(20), unique=True, nullable=False)

    ifsc_code = db.Column(db.String(20), nullable=False, default="VGBI0001234")

    balance = db.Column(db.Float, default=50000.00)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    transactions = db.relationship(
        "Transaction",
        backref="user",
        lazy=True,
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<User {self.email}>"