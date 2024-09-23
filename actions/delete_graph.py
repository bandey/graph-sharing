from database.models import graph, vertex, edge

def deleteGraph(id):
  edge.deleteByGraphId(id)
  vertex.deleteByGraphId(id)
  graph.delete(id)
