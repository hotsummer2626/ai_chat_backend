from dotenv import load_dotenv
load_dotenv()
from flask import Flask
import config
from exts import db, ma
from blueprints import api
from models import User
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(config)
db.init_app(app)
JWTManager(app)
migrate = Migrate(app, db)
ma.init_app(app)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
