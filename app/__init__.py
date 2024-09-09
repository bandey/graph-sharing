from flask import Flask

# create application instance
app = Flask(__name__)

# init extensions

# import views
from . import router
