
import os
from flask import Flask

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")

if not app.secret_key:
    raise RuntimeError(
        "Не задано SECRET_KEY для Flask"
    )

from app import views
from app.users import users
from app.products import products

app.register_blueprint(users)
app.register_blueprint(products)
