from webserver import app
from bcrypt import checkpw
from flask import session
from database.models import visitor

def enter(email, passw):
  if (not email) or (not passw):
    return 'Некорректные email или пароль'
  email = email.strip().lower()
  if (len(email) < 1) or (len(passw) < 1):
    return 'Некорректные email или пароль'

  candidate = visitor.getOneByEmail(email)
  if not candidate:
    return 'Неверные email или пароль'
  try:
    isEqu = checkpw(passw.encode(), candidate['password'].encode())
  except Exception as err:
    return 'Неверные email или пароль'
  if not isEqu:
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
