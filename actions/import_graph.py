import json
from database.models import vertex

def importGraph(file):
  file.seek(0)
  buffBinary = file.read()
  buffString = buffBinary.decode()
  data = json.loads(buffString)
  vertex.insert(data)
  return 'Данные из файла успешно импортированы'
