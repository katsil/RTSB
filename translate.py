import requests, gamekeeper as tool, config

def translate(bot, update):
  # part with token
  key = '?key=' + config.TRANSLATE_TOKEN
  # part with text from user (all message without '/tr')
  toTranslate = '&text=' + tool.getCore(update, 'tr')
  # url for checking language of text
  urlCheck = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
  urlCheck += key + toTranslate
  # url for translating 
  url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
  url += key + toTranslate
  # geting language of user's text
  lang = requests.get(urlCheck)
  # if it's RU - translate to EN, else - translate to RU
  if lang.json()['lang'] == 'ru':
    url += '&lang=en'
  else:
    url += '&lang=ru'
  # send result back
  text = requests.get(url).json()['text'][0]
  tool.sendTextBack(text, update, bot)