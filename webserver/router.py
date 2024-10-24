from webserver import app
from flask import request, session, redirect, url_for, flash, render_template
from actions.import_graph import importGraph
from actions.save_graph import saveGraph
from actions.delete_graph import deleteGraph
from database.models import graph, vertex, edge

@app.route('/')
def route_index():
  if 'visitor' in session:
    return render_template('list.html', graphs=graph.getAll())
  else:
    return redirect(url_for('route_auth'))

@app.route('/auth')
def route_auth():
  return render_template('login-form.html')

@app.route('/auth/enter', methods=['POST'])
def route_auth_enter():
  if ((request.form['login'] == app.config['HARD_LOGIN']) and 
      (request.form['passw'] == app.config['HARD_PASSW'])):
    session['visitor'] = request.form['login']
    return redirect(url_for('route_index'))
  else:
    return render_template('login-form.html')

@app.route('/auth/exit', methods=['GET', 'POST'])
def route_auth_exit():
  session.pop('visitor', None)  
  return redirect(url_for('route_auth'))

@app.route('/import', methods=['GET', 'POST'])
def route_import():
  if 'visitor' not in session:
    return redirect(url_for('route_auth'))
  if request.method == 'GET':
    return render_template('import.html')
  if 'graphName' not in request.form:
    flash('Не указано имя графа')
    return render_template('import.html')
  if 'dataFile' not in request.files:
    flash('Не выбран файл для импорта')
    return render_template('import.html')
  file = request.files['dataFile']
  if file.filename == '':
    flash('Не выбран файл для импорта')
    return render_template('import.html')
  name = request.form['graphName']
  result = importGraph(file, name)
  flash(result)
  return render_template('result.html')

@app.route('/s/<id>')
def route_s(id):
  m = 'show'
  if 'visitor' in session:
    m = 'edit'
  g = graph.getOne(id)
  if not g:
    flash('Ошибка: Указанный граф не найден')
    return render_template('result.html')
  vs = vertex.getByGraphId(id)
  es = edge.getByGraphId(id)
  return render_template('show.html', mode=m, graph=g, vertices=vs, edges=es)

@app.route('/save/<id>', methods=['POST'])
def route_save(id):
  if 'visitor' not in session:
    return redirect(url_for('route_auth'))
  data = request.form['jsonData']
  result = saveGraph(id, data)
  flash(result)
  return render_template('result.html')

@app.route('/delete/<id>', methods=['POST'])
def route_delete(id):
  if 'visitor' not in session:
    return redirect(url_for('route_auth'))
  deleteGraph(id)
  return redirect(url_for('route_index'))
