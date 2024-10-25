from database import dbClient

def getOneByEmail(email):
  visitor = dbClient().visitors.find_one({'email': email})
  return visitor
