import json
from database.models import vertex

def importGraph(file):
  # go to begin of file
  file.seek(0)
  # read binary data and decode it to string
  buffBinary = file.read()
  buffString = buffBinary.decode()
  # parse json string
  data = json.loads(buffString)
  # get root object
  root = data[0]

  # loop all persons
  for elem in root['persons']:
    # rename special fields _id and _key
    elem['id'] = elem['_id']
    del elem['_id']
    elem['key'] = elem['_key']
    del elem['_key']
    # save person in database
    vertex.insert(elem)
  
  return 'Данные из файла успешно импортированы'
