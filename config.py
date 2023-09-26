import os

HOSTNAME = os.getenv("DB_HOSTNAME")
PORT = '3306'
DATABASE = 'ai_chat'
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
