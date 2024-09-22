from database import dbClient

def insert(graph):
  result = dbClient().gs_graph.insert_one(graph)
  return result.inserted_id
