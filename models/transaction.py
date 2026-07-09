from models.user import db

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)

    # Relationship with User
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    sender_id = db.Column(db.Integer, nullable=False)
    receiver_id = db.Column(db.Integer, nullable=False)

    sender_email = db.Column(db.String(100), nullable=False)
    receiver_email = db.Column(db.String(100), nullable=False)

    receiver_name = db.Column(db.String(100), nullable=False)

    amount = db.Column(db.Float, nullable=False)

    # NEW COLUMN
    transaction_type = db.Column(db.String(20), nullable=False)

    status = db.Column(db.String(20), default="Success")

    transaction_date = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )