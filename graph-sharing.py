from database import dbConnect
from webserver import app

if __name__ == '__main__':
  dbConnect(app=app, uri=app.config['DB_CONNECT'])
  app.run(host=app.config['SERV_HOST'], port=app.config['SERV_PORT'])
