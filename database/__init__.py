from flask_pymongo import PyMongo

dbH = None

def dbConnect(app, uri):
  global dbH
  dbH = PyMongo(app, uri).db
  return dbH

def dbClient():
  global dbH
  return dbH
