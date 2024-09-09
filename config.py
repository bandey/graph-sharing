import os

class Config:
  DEBUG = os.environ.get('FLASK_DEBUG') or False
  SERV_PORT = os.environ.get('SERV_PORT') or 8080
