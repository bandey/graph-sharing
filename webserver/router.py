from webserver import app
from flask import request, session, redirect, url_for, flash, render_template
from actions.import_graph import importGraph
from actions.delete_graph import deleteGraph
from database.models import graph, vertex

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
  session['visitor'] = request.form['login']
  return redirect(url_for('route_index'))

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
  g = graph.getOne(id)
  vs = vertex.getByGraphId(id)
  return render_template('show.html', graph=g, vertices=vs)

@app.route('/delete/<id>', methods=['POST'])
def route_delete(id):
  if 'visitor' not in session:
    return redirect(url_for('route_auth'))
  deleteGraph(id)
  return redirect(url_for('route_index'))
