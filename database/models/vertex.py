from database import dbClient

def insert(vertex):
  dbClient().gs_vertex.insert_one(vertex)
