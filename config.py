import os

class Config:
  DEBUG = os.environ.get('FLASK_DEBUG') or False
  SERV_HOST = os.environ.get('TASK_SERV_HOST') or '0.0.0.0'
  SERV_PORT = os.environ.get('TASK_SERV_PORT') or 8080
  DB_CONNECT = os.environ.get('TASK_DB_CONNECT') or 'mongodb://localhost/test'
  SECRET_KEY = os.environ.get('TASK_SECRET_KEY') or 'A_SECRET_KEY'
