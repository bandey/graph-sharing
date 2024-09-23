from database import dbClient
from bson.objectid import ObjectId

def insert(graph):
  result = dbClient().gs_graph.insert_one(graph)
  return result.inserted_id

def getAll():
  graphs = dbClient().gs_graph.find()
  return graphs

def delete(id):
  result = dbClient().gs_graph.delete_one({'_id': ObjectId(id)})
  return result
