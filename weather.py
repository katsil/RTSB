import telegram, requests, gamekeeper as tool, config
from telegram import replykeyboardmarkup, replykeyboardremove

# dict of cities, may be expanded manually
def getCityBase():
  cityBase ={
    'Moscow':'ru',
    'Saint Petersburg':'ru',
    'Rostov':'ru',
    'Ryazan':'ru',
    'Kaluga':'ru',
    'Volgograd':'ru',
    'Orel':'ru',
    'London':'gb',
    'York':'gb',
    'Kiev':'ua',
    'Minsk':'by',
    'Brest':'by',
  }
  return cityBase

#transform array into matrix with 3 cols
def createArray3(arr):
  keyBoard = []
  temp = []
  i=1
  for city in arr.keys():
    temp.append(city)
    if i%3==0:
      keyBoard.append(temp)
      temp = []
    i+=1
  if i%3!=1:
    keyBoard.append(temp)
  return keyBoard

def weatherRequest(bot, update):
  cityBase = getCityBase()
  keyBoardArray = createArray3(cityBase) # prepare custom keyboard 
  keyBoard = telegram.ReplyKeyboardMarkup(keyBoardArray, one_time_keyboard=True) # create keyboard
  tool.sendTextBack('Choose and i will give you advise about umbrella', update, bot, keyBoard) # shoot keyboard into user

def weatherBack(update, bot, name, country):
  key = '?APPID=' + config.WEATHER_TOKEN
  url = 'http://api.openweathermap.org/data/2.5/forecast' + key 
  url += '&cnt=6&units=metric' # parametrs
  url += '&q={},{}'.format(name.replace(' ','+'), country) # + is for names more then one word
  remover = telegram.ReplyKeyboardRemove() # remove custom keyboard 
  res = requests.get(url).json()
  # it will catch forecast for every 3 hours in nearest future
  # parametr cnt=6 define that only 6 parts will come
  counter=0
  for each in res['list']:
    if each['weather'][0]['main'] == 'Rain':
      counter += 1
  if counter > 4: # if rain in 5/6 or 6/6 
    tool.sendTextBack('only with umbrella', update, bot, remover)
  elif counter >1: # if rain in 2/6, 3/6 or 4/6
    tool.sendTextBack('better with umbrella', update, bot, remover)
  else: # 0/6 or 1/6
    tool.sendTextBack('leave it at home', update, bot, remover)
    