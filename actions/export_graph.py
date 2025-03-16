from database.models import graph, vertex, edge

def exportGraph(id):
  g = graph.getOne(id)
  if not g:
    return None

  r = {}

  kind = g.get('kind', '')
  if kind:
    r['kind'] = kind

  layout = g.get('layout', '')
  if layout:
    r['layout'] = layout

  # loop all vertices
  vs = vertex.getByGraphId(id)
  vertices = []
  for elem in vs:
    # rename special fields _id and _key
    elem['_id'] = elem['id']
    del elem['id']
    elem['_key'] = elem['key']
    del elem['key']
    # drop some field
    del elem['class']
    del elem['graph_id']
    vertices.append(elem)

  # loop all edges
  es = edge.getByGraphId(id)
  edges = []
  for elem in es:
    # rename special fields _id, _from and _to
    elem['_id'] = elem['id']
    del elem['id']
    elem['_from'] = elem['source']
    del elem['source']
    elem['_to'] = elem['target']
    del elem['target']
    # drop some field
    del elem['class']
    del elem['graph_id']
    edges.append(elem)

  r['vertices'] = vertices
  r['edges'] = edges

  return [r]
