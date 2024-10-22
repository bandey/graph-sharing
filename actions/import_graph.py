import json
from database.models import graph, vertex, edge

def importGraph(file, name):
  # go to begin of file
  file.seek(0)
  # read binary data and decode it to string
  buffBinary = file.read()
  buffString = buffBinary.decode()
  # parse json string
  data = json.loads(buffString)
  # get root object
  root = data[0]

  # add new graph to database
  graph_id = graph.insert({'name': name})

  # loop all vertices
  for elem in root['vertices']:
    # rename special fields _id and _key
    elem['id'] = elem['_id']
    del elem['_id']
    elem['key'] = elem['_key']
    del elem['_key']
    # drop special field _rev
    del elem['_rev']
    # add class field
    elem['class'] = elem['id'].split('/',1)[0]
    # add graph_id field
    elem['graph_id'] = graph_id
    # save vertex in database
    vertex.insert(elem)

  # loop all edges
  for elem in root['edges']:
    # rename special fields _id, _from and _to
    elem['id'] = elem['_id']
    del elem['_id']
    elem['source'] = elem['_from']
    del elem['_from']
    elem['target'] = elem['_to']
    del elem['_to']
    # drop special fields _key and _rev
    del elem['_key']
    del elem['_rev']
    # add class field
    elem['class'] = elem['id'].split('/',1)[0]
    # add graph_id field
    elem['graph_id'] = graph_id
    # save edge in database
    edge.insert(elem)
  
  return 'Данные из файла успешно импортированы'
