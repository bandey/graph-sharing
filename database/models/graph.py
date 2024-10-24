from database import dbClient
from bson.objectid import ObjectId

def insert(graph):
  result = dbClient().gs_graph.insert_one(graph)
  return result.inserted_id

def getAll():
  graphs = dbClient().gs_graph.find().sort('name')
  return graphs

def getOne(id):
  graph = dbClient().gs_graph.find_one({'_id': ObjectId(id)})
  return graph

def getOneByName(name):
  graph = dbClient().gs_graph.find_one({'name': name})
  return graph

def update(id, modifier):
  result = dbClient().gs_graph.find_one_and_update({'_id': ObjectId(id)}, {'$set': modifier})
  return result

def delete(id):
  result = dbClient().gs_graph.delete_one({'_id': ObjectId(id)})
  return result
