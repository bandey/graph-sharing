from database.models import graph, vertex, edge

def embraceArr(inpArr):
  resArr = []
  for val in inpArr:
    resArr.extend([val, '[' + val + ']', '(' + val + ')'])
  return resArr

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
      if elem['name'] in embraceArr(['супруг', 'супруга']):
        elem['class'].append('relate-married')
      elif not elem['name'] in embraceArr(['брат', 'сестра', 'сын', 'дочь',
          'отец', 'мать','внук', 'внучка', 'дедушка', 'бабушка']):
        elem['class'].append('relate-distant')
    else:
      elem['label'] = elem['name']
    edges.append(elem)

  g['vertices'] = vertices
  g['edges'] = edges

  return g
