# 🏦 Vaishnavi Gramin Bank

A modern Banking Web Application built using **Python, Flask, MySQL, HTML, CSS, Bootstrap, and JavaScript**.

This project simulates an online banking system where users can create an account, log in securely, manage their profile, transfer money, and view transaction history.

---

# 📌 Features

## 🔐 Authentication
- User Registration
- Secure Login
- Password Hashing
- Session Management
- Logout

---

## 👤 User Profile

- View Profile
- Edit Profile
- Update Phone Number
- Update Address
- View Account Details
- View IFSC Code
- View UPI ID

---

## 💰 Banking Features

- Auto Generated Account Number
- Auto Generated Debit Card Number
- Auto Generated UPI ID
- Default Balance
- Balance Hide/Show
- Money Transfer
- Live Balance Update
- Transaction History

---

## 💳 Dashboard

- Professional Banking UI
- Sidebar Navigation
- Navbar
- Balance Card
- Premium ATM Card
- Quick Actions
- User Information
- Responsive Layout

---

## 📜 Transaction Management

- Credit Transactions
- Debit Transactions
- Transaction Status
- Receiver Details
- Transaction Date & Time

---

## 🗄 Database

- MySQL Database
- SQLAlchemy ORM
- User Table
- Transaction Table

---

# 🛠 Technologies Used

### Backend

- Python
- Flask
- SQLAlchemy
- Werkzeug

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons
- JavaScript

### Database

- MySQL

---

# 📂 Project Structure

```
bank-app-aws/

│

├── app.py

├── config.py

├── requirements.txt

│

├── models/

│ ├── user.py

│ └── transaction.py

│

├── templates/

│ ├── login.html

│ ├── register.html

│ ├── dashboard.html

│ ├── profile.html

│ ├── transfer.html

│ ├── history.html

│ ├── settings.html

│ └── components/

│

├── static/

│ ├── css/

│ ├── js/

│ ├── images/

│ └── uploads/

│

└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/rohanbadnale/bank-app-aws.git
```

Go to project

```bash
cd bank-app-aws
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Project

```bash
python app.py
```

---

# 🗄 Configure Database

Create MySQL Database

```sql
CREATE DATABASE bank_db;
```

Update your **config.py**

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/bank_db"
```

Run Project

```bash
python app.py
```

---

# 📷 Screens

- Login Page
- Register Page
- Dashboard
- Profile
- Money Transfer
- Transaction History

*(Screenshots can be added later.)*

---

# 🚀 Upcoming Features

- Profile Photo Upload
- Change Password
- Premium Debit Card Page
- ATM Card Flip Animation
- PDF Statement Download
- Email Notifications
- Charts & Analytics
- Dark Mode
- Mobile Responsive UI
- AWS EC2 Deployment
- AWS RDS Integration
- Nginx + Gunicorn Deployment
- SSL (HTTPS)

---

# 🎯 Learning Outcomes

This project helped in understanding:

- Flask Framework
- MVC Architecture
- SQLAlchemy ORM
- MySQL Integration
- Authentication
- Password Hashing
- Session Handling
- CRUD Operations
- Banking System Design
- Responsive Dashboard Design

---

# 👨‍💻 Developer

**Rohan Badnale**

Bachelor of Computer Applications (BCA)

Cloud & DevOps Enthusiast

GitHub

https://github.com/rohanbadnale

---

# ⭐ Repository

If you like this project, don't forget to ⭐ Star the repository.

---

# 📄 License

This project is developed for educational and portfolio purposes.
