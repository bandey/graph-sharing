from webserver import app
from flask import request, session, redirect, url_for, render_template

@app.route('/')
def index():
  if 'visitor' in session:
    return render_template('hello.html')
  else:
    return redirect(url_for('auth'))

@app.route('/auth')
def auth():
  return render_template('login-form.html')

@app.route('/auth/enter', methods=['POST'])
def auth_enter():
  session['visitor'] = request.form['login']
  return redirect(url_for('index'))

@app.route('/auth/exit', methods=['GET', 'POST'])
def auth_exit():
  session.pop('visitor', None)  
  return redirect(url_for('auth'))

@app.route('/import', methods=['GET', 'POST'])
def route_import():
  if 'visitor' not in session:
    return redirect(url_for('auth'))
  if request.method == 'GET':
    return render_template('import.html')
  if 'dataFile' not in request.files:
    return render_template('import.html')
  file = request.files['dataFile']
  if file.filename == '':
    return render_template('import.html')
  file.seek(0)
  binary = file.read()
  stroka = binary.decode()
  return render_template('hello.html')
