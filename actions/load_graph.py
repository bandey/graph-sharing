from database.models import graph, vertex, edge

def loadGraph(id):
  g = graph.getOne(id)
  if not g:
    return None
  g['vertices'] = vertex.getByGraphId(id)
  g['edges'] = edge.getByGraphId(id)
  return g
