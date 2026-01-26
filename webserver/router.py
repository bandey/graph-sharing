from webserver import app
from flask import request, Response, redirect, url_for, json, flash, render_template
from . import auth
from actions.import_graph import importGraph
from actions.load_graph import loadGraph
from actions.save_graph import saveGraph
from actions.delete_graph import deleteGraph
from actions.export_graph import exportGraph
from database.models import graph

@app.route('/')
def route_index():
  if auth.check():
    return render_template('list.html', graphs=graph.getAll())
  else:
    return redirect(url_for('route_auth'))

@app.route('/auth')
def route_auth():
  return render_template('login-form.html')

@app.route('/auth/enter', methods=['POST'])
def route_auth_enter():
  errMsg = auth.enter(request.form.get('login'), request.form.get('passw'))
  if errMsg:
    flash(errMsg)
    return render_template('login-form.html')
  return redirect(url_for('route_index'))

@app.route('/auth/exit', methods=['GET', 'POST'])
def route_auth_exit():
  auth.exit()
  return redirect(url_for('route_auth'))

@app.route('/import', methods=['GET', 'POST'])
def route_import():
  if not auth.check():
    return redirect(url_for('route_auth'))
  if request.method == 'GET':
    return render_template('import.html')
  file = request.files.get('dataFile')
  if (not file) or (not file.filename):
    flash('Не выбран файл для импорта')
    return render_template('import.html')
  optReplace = True if request.form.get('optReplace') else False
  result = importGraph(file, request.form.get('graphName', ''), optReplace)
  flash(result)
  return render_template('result.html')

@app.route('/s/<id>')
def route_s(id):
  m = 'edit' if auth.check() else 'show'
  g = loadGraph(id)
  if not g:
    flash('Ошибка: Указанный граф не найден')
    return render_template('result.html')
  return render_template('show.html', mode=m, graph=g)

@app.route('/save/<id>', methods=['POST'])
def route_save(id):
  if not auth.check():
    return redirect(url_for('route_auth'))
  result = saveGraph(id, request.form.get('jsonData', ''))
  flash(result)
  return render_template('result.html')

@app.route('/delete/<id>', methods=['POST'])
def route_delete(id):
  if not auth.check():
    return redirect(url_for('route_auth'))
  deleteGraph(id)
  return redirect(url_for('route_index'))

@app.route('/export/<id>')
def route_export(id):
  sJson = ''
  if not auth.check():
    sJson = json.dumps({'error': 'Not authorized'})
  else:
    g = exportGraph(id)
    if not g:
      sJson = json.dumps({'error': 'Graph not found'})
    else:
      sJson = json.dumps(g, ensure_ascii=False, sort_keys=False)
  return Response(sJson, content_type='application/json; charset=utf-8')
