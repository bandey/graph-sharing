from webserver import app
from flask import session

def enter(email, passw):
  if (not email) or (not passw):
    return 'Некорректные email или пароль'
  email = email.strip()
  if (len(email) < 1) or (len(passw) < 1):
    return 'Некорректные email или пароль'

  if (email != app.config['HARD_LOGIN']) or (passw != app.config['HARD_PASSW']):
    return 'Неверные email или пароль'

  session['visitor'] = email
  return ''

def check():
  if 'visitor' in session:
    return True
  else:
    return False

def exit():
  session.pop('visitor', None)
