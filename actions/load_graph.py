from database.models import graph, vertex, edge

def loadGraph(id):
  g = graph.getOne(id)
  if not g:
    return None
  kind = g.get('kind', '')

  vs = vertex.getByGraphId(id)
  es = edge.getByGraphId(id)

  # Decorate vertices
  vertices = []
  for elem in vs:
    elem['label'] = elem['name']
    vertices.append(elem)

  # Decorate edges
  edges = []
  for elem in es:
    if kind == 'relatives':
      elem['label'] = '%s [%s]' % (elem['name'], ','.join(elem['origins']))
    else:
      elem['label'] = elem['name']
    edges.append(elem)

  g['vertices'] = vertices
  g['edges'] = edges

  return g
