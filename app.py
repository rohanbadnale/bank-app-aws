from flask import Flask, render_template, request, redirect, url_for, session
from config import Config
from models.user import db, User
from models.transaction import Transaction
from werkzeug.security import generate_password_hash, check_password_hash
import random
app = Flask(__name__)
app.secret_key = "vaishnavi_bank_secret"
app.config.from_object(Config)

db.init_app(app)


# ---------------- HOME ----------------
@app.route("/")
def home():
    return redirect(url_for("login"))


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        # Find user by email only
        user = User.query.filter_by(email=email).first()

        # Verify hashed password
        if user and check_password_hash(user.password, password):

            session["user_id"] = user.id

            return redirect(url_for("dashboard"))

        return "<h3>❌ Invalid Email or Password</h3>"

    return render_template("login.html")


# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Check Password Match
        if password != confirm_password:
            return "<h3>❌ Passwords do not match.</h3>"

        # Check Existing Email
        existing = User.query.filter_by(email=email).first()

        if existing:
            return "<h3>❌ Email already exists.</h3>"

        # Hash Password
        hashed_password = generate_password_hash(password)

        # Generate Account Number
        account_number = str(random.randint(100000000000, 999999999999))

        # Generate Card Number
        card_number = (
            str(random.randint(4000, 4999)) + " " +
            str(random.randint(1000, 9999)) + " " +
            str(random.randint(1000, 9999)) + " " +
            str(random.randint(1000, 9999))
        )

        # Generate UPI
        upi_id = email.split("@")[0] + "@vaishnavi"

        new_user = User(
            fullname=fullname,
            email=email,
            password=hashed_password,
            phone="",
            address="",
            account_number=account_number,
            ifsc_code="VGBI0001234",
            balance=50000,
            card_number=card_number,
            upi_id=upi_id
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")
# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    return render_template(
        "dashboard.html",
        user=user
    )

# ---------------- TRANSFER ----------------
@app.route("/transfer", methods=["GET", "POST"])
def transfer():

    if "user_id" not in session:
        return redirect(url_for("login"))

    sender = User.query.get(session["user_id"])

    if request.method == "POST":

        account_number = request.form["account_number"]
        amount = float(request.form["amount"])

        receiver = User.query.filter_by(
            account_number=account_number
        ).first()

        if receiver is None:
            return "<h3>❌ Receiver Account Not Found</h3>"

        if sender.id == receiver.id:
            return "<h3>❌ You cannot transfer money to your own account.</h3>"

        if sender.balance < amount:
            return "<h3>❌ Insufficient Balance</h3>"

        # Update Balance
        sender.balance -= amount
        receiver.balance += amount

        # Sender Transaction
        sender_transaction = Transaction(
            user_id=sender.id,
            sender_id=sender.id,
            receiver_id=receiver.id,
            sender_email=sender.email,
            receiver_email=receiver.email,
            receiver_name=receiver.fullname,
            amount=amount,
            transaction_type="DEBIT",
            status="Success"
        )

        # Receiver Transaction
        receiver_transaction = Transaction(
            user_id=receiver.id,
            sender_id=sender.id,
            receiver_id=receiver.id,
            sender_email=sender.email,
            receiver_email=receiver.email,
            receiver_name=sender.fullname,
            amount=amount,
            transaction_type="CREDIT",
            status="Success"
        )

        db.session.add(sender_transaction)
        db.session.add(receiver_transaction)

        db.session.commit()

        return redirect(url_for("history"))

    return render_template("transfer.html")


# ---------------- HISTORY ----------------
@app.route("/history")
def history():

    if "user_id" not in session:
        return redirect(url_for("login"))

    transactions = Transaction.query.filter_by(
        user_id=session["user_id"]
    ).order_by(
        Transaction.transaction_date.desc()
    ).all()

    return render_template(
        "history.html",
        transactions=transactions
    )


# ---------------- BENEFICIARY ----------------
@app.route("/beneficiary")
def beneficiary():
    return render_template("beneficiary.html")


# ---------------- CARDS ----------------
@app.route("/cards")
def cards():
    return render_template("cards.html")


# ---------------- BILL PAYMENTS ----------------
@app.route("/bills")
def bills():
    return render_template("bills.html")


# ---------------- RECHARGE ----------------
@app.route("/recharge")
def recharge():
    return render_template("recharge.html")


# ---------------- PROFILE ----------------
@app.route("/profile", methods=["GET", "POST"])
def profile():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    if request.method == "POST":

        user.fullname = request.form["fullname"]
        user.phone = request.form["phone"]
        user.address = request.form["address"]

        db.session.commit()

        return redirect(url_for("profile"))

    return render_template(
        "profile.html",
        user=user
    )


# ---------------- SETTINGS ----------------
@app.route("/settings")
def settings():
    return render_template("settings.html")

# ---------------- DASHBOARD V2 ----------------
@app.route("/dashboard-v2")
def dashboard_v2():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    return render_template(
        "dashboard_v2.html",
        user=user
    )


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    return redirect(url_for("login"))


# ---------------- RUN ----------------
if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)