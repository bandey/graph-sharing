import json
from database.models import graph, vertex

def saveGraph(graphId, jsonData):
  # parse json string
  data = json.loads(jsonData)

  # loop all vertices
  for elem in data:
    vertex.updateByIds(graphId, elem['id'], {'x': elem['x'], 'y': elem['y']})

  graph.update(graphId, {'layout': 'preset'})

  return 'Данные успешно сохранены'