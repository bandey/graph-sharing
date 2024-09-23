from database import dbClient
from bson.objectid import ObjectId

def insert(edge):
  result = dbClient().gs_edge.insert_one(edge)
  return result.inserted_id

def deleteByGraphId(graphId):
  result = dbClient().gs_edge.delete_many({'graph_id': ObjectId(graphId)})
  return result
