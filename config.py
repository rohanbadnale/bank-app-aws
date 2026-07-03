class Config:
    SECRET_KEY = "bank123"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/bank_db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False