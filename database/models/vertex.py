from database import dbClient

def insert(vertex):
  result = dbClient().gs_vertex.insert_one(vertex)
  return result.inserted_id
