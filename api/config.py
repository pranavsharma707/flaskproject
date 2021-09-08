from app import flaskAppInstance
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

# new
# Create the SQLAlchemy db instance
SQLALCHEMY_DATABASE_URL = "postgresql://myuser:mypass@127.0.0.1:5432/flaskdb"
flaskAppInstance.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URL
flaskAppInstance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(flaskAppInstance) 
# db.init_app(flaskAppInstance)

# migrate = Migrate(flaskAppInstance,db)

ma = Marshmallow(flaskAppInstance)