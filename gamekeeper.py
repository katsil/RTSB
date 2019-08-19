# geting text of message without command 
def getCore(update, command):
  name = update.message.text[len(command)+1:] # '/' is +1
  return name.strip()

# send text back to user from update object
def sendTextBack(text, update, bot, repl = None): 
  bot.send_message(
    chat_id = update.message.chat_id,
    text = text,
    reply_markup = repl, # for attaching keyboard or so
  )