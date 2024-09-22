from webserver import app
from flask import request, session, redirect, url_for, flash, render_template

@app.route('/')
def route_index():
  if 'visitor' in session:
    return render_template('hello.html')
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
  if 'dataFile' not in request.files:
    flash('Не выбран файл для импорта')
    return render_template('import.html')
  file = request.files['dataFile']
  if file.filename == '':
    flash('Не выбран файл для импорта')
    return render_template('import.html')
  file.seek(0)
  binary = file.read()
  stroka = binary.decode()
  flash('Данные из файла успешно импортированы')
  return render_template('import.html')
