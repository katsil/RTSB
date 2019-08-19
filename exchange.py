import requests, xml, gamekeeper as tool, xml.dom.minidom

# list of valutes, may ne expand manualy
requiredValutes = ('USD', 'EUR', 'CNY', 'JPY')

def exchange(bot, update):
  # universal url, no token needed
  url = 'http://www.cbr.ru/scripts/XML_daily.asp'
  res = requests.get(url)
  xm = xml.dom.minidom.parseString(res.content) # grab xml
  valuteList = xm.getElementsByTagName('Valute') # incoming list of valutes
  data = xm.getElementsByTagName('ValCurs')[0].getAttribute('Date') # date
  text = 'Exchange rate for today ({}):\n'.format(data)
  for valute in valuteList:
    if valute.getElementsByTagName('CharCode')[0].firstChild.data in requiredValutes:
      name = valute.getElementsByTagName('CharCode')[0].firstChild.data
      value = valute.getElementsByTagName('Value')[0].firstChild.data
      text += '{} - {}\n'.format(name, value)
  tool.sendTextBack(text, update, bot)
