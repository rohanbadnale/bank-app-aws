from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    # Personal Details
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    phone = db.Column(db.String(15))
    address = db.Column(db.String(255))

    # Banking Details
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    ifsc_code = db.Column(db.String(20), nullable=False)

    balance = db.Column(db.Float, default=50000.00)

    card_number = db.Column(db.String(25), unique=True)

    upi_id = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f"<User {self.fullname}>"