from flask import Flask
import config

# create application instance
app = Flask(__name__)
app.config.from_object('config.Config')

# init extensions

# import views
from . import router
