import json
from database.models import graph, vertex
from bson.objectid import ObjectId

def saveGraph(graphId, jsonData):
  # check if graph with given id not exist
  if not graph.getOne(graphId):
    return 'Ошибка: Указанный граф не найден'

  # parse json string
  try:
    data = json.loads(jsonData)
  except Exception as err:
    return 'Ошибка: Невозможно разобрать json-строку'

  # check given graph name
  graphName = data.get('name', '')
  if len(graphName) < 1:
    return 'Ошибка: Не указано имя графа'
  # check if another graph with given name already exist
  testGraph = graph.getOneByName(graphName)
  if testGraph and (testGraph['_id'] != ObjectId(graphId)):
    return 'Ошибка: Граф с указанным названием уже есть'

  # loop all vertices
  for elem in data.get('pos', []):
    vertex.updateByIds(graphId, elem['id'], {'x': elem['x'], 'y': elem['y']})

  graph.update(graphId, {'name': graphName, 'layout': 'preset'})

  return 'Данные успешно сохранены'