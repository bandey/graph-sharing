from database import dbClient
from bson.objectid import ObjectId

def insert(vertex):
  result = dbClient().gs_vertex.insert_one(vertex)
  return result.inserted_id

def getByGraphId(graphId):
  vertices = dbClient().gs_vertex.find({'graph_id': ObjectId(graphId)})
  return vertices

def deleteByGraphId(graphId):
  result = dbClient().gs_vertex.delete_many({'graph_id': ObjectId(graphId)})
  return result
