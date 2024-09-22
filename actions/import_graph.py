import json
from database.models import graph, vertex

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

  # loop all persons
  for elem in root['persons']:
    # rename special fields _id and _key
    elem['id'] = elem['_id']
    del elem['_id']
    elem['key'] = elem['_key']
    del elem['_key']
    # add graph_id field
    elem['graph_id'] = graph_id
    # save person in database
    vertex.insert(elem)
  
  return 'Данные из файла успешно импортированы'
