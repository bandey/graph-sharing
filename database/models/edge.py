from database import dbClient

def insert(edge):
  result = dbClient().gs_edge.insert_one(edge)
  return result.inserted_id
