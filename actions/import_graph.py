import json
from database.models import graph, vertex, edge
from actions.delete_graph import deleteGraph

def importGraph(file, name, optReplace):
  # check given graph name
  graphName = name.strip()
  if len(graphName) < 1:
    return 'Ошибка: Не указано имя графа'

  # check if graph with given name already exist
  g = graph.getOneByName(graphName)
  graph_id = g.get('_id', '') if g else ''
  if graph_id:
    if optReplace:
      deleteGraph(graph_id)
    else:
      return 'Ошибка: Граф с указанным названием уже есть'

  # go to begin of file
  file.seek(0)
  # read binary data and decode it to string
  try:
    buffBinary = file.read()
    buffString = buffBinary.decode()
  except Exception as err:
    return 'Ошибка: Невозможно декодировать файл'

  # parse json string
  try:
    data = json.loads(buffString)
  except Exception as err:
    return 'Ошибка: Невозможно разобрать json-файл'
  # get root object
  root = data[0]

  # add new graph to database
  graphBody = {'name': graphName, 'kind': root.get('kind', ''), 
    'layout': root.get('layout', '')};
  if graph_id:
    graphBody['_id'] = graph_id
  graph_id = graph.insert(graphBody)

  # loop all vertices
  for elem in root.get('vertices', []):
    # rename special fields _id and _key
    elem['id'] = elem['_id']
    del elem['_id']
    elem['key'] = elem['_key']
    del elem['_key']
    # drop special field _rev
    if '_rev' in elem:
      del elem['_rev']
    # add class field
    elem['class'] = [elem['id'].split('/',1)[0]]
    # add graph_id field
    elem['graph_id'] = graph_id
    # save vertex in database
    vertex.insert(elem)

  # loop all edges
  for elem in root.get('edges', []):
    # rename special fields _id, _from and _to
    elem['id'] = elem['_id']
    del elem['_id']
    elem['source'] = elem['_from']
    del elem['_from']
    elem['target'] = elem['_to']
    del elem['_to']
    # drop special fields _key and _rev
    if '_key' in elem:
      del elem['_key']
    if '_rev' in elem:
      del elem['_rev']
    # add class field
    elem['class'] = [elem['id'].split('/',1)[0]]
    # add graph_id field
    elem['graph_id'] = graph_id
    # save edge in database
    edge.insert(elem)
  
  return 'Данные из файла успешно импортированы'
