from webserver import app

if __name__ == '__main__':
  app.run(host=app.config['SERV_HOST'], port=app.config['SERV_PORT'])
