import sqlite3, gamekeeper as tool

# check entry
def isUserExists(wand, name):
  wand.execute("SELECT count(*) FROM users WHERE name = ?", [(name)])
  if wand.fetchone()[0] > 0:
    return True
  else:
    return False

def reg(bot, update):
  # connection
  ZConnection = sqlite3.connect("OneWayUsing.db") 
  wand = ZConnection.cursor()
  name = tool.getCore(update, 'reg') # get message without command
  if len(name)< 3: # say no if it's too short
    text = 'Too short name'
  elif isUserExists(wand, name):
    text = 'User {} already exists, chose other name'.format(name)
  else:
    wand.execute("INSERT INTO users VALUES (?,NULL)", [name])
    ZConnection.commit() # adding
    text = 'User {} added'.format(name)
  tool.sendTextBack(text, update, bot) # send an answer

  # have no idea what login is planed for, but it was in task
def login(bot, update):
  # connection
  ZConnection = sqlite3.connect("OneWayUsing.db") 
  wand = ZConnection.cursor()
  name = tool.getCore(update, 'login') # get message without command
  if len(name)< 3: # say no if it's too short
    text = 'Too short name'
  elif isUserExists(wand, name):
    text = 'You loggen in as {}'.format(name) # calm user down
  else:
    text = 'User {} does not exists. Use "/reg {}" to solve'.format(name, name)
  tool.sendTextBack(text, update, bot) # send an answer