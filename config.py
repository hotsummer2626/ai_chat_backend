import os

HOSTNAME = os.getenv("DB_HOSTNAME")
PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("DB_NAME")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
