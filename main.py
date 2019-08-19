import telegram, config, gamekeeper as tool, translate, basePart, weather, exchange
from telegram import Bot, Update, Message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# handle common messgaes (without commands)
def commonMessage(bot: Bot, update: Update):
  cityBase = weather.getCityBase()
  text = update.message.text
  if text in cityBase.keys(): # checking cities for weather forecast
    weather.weatherBack(update, bot, text, cityBase[text])

def translateCall(bot: Bot, update: Update):
  translate.translate(bot, update)

def regCall(bot: Bot, update: Update):
  basePart.reg(bot, update)

def loginCall(bot: Bot, update: Update):
  basePart.login(bot, update)

def weatherCall(bot: Bot, update: Update):
  weather.weatherRequest(bot, update)

def exchangeCall(bot: Bot, update: Update):
  exchange.exchange(bot, update)

def helpCall(bot: Bot, update: Update):
  text = '''You can use next commands for free:
/translate - translate text from any language to Russian or from Russian to English
Example: /translate test
/weather - ask about your umbrella for tomorrow. Choose your city
/reg - register a new user by name
/login - login as existing user by name
Example: /login test1'''
  tool.sendTextBack(text, update, bot)

def test(bot: Bot, update: Update):
  pass
  

def main():
  bot = Bot(
    token = config.BOT_TOKEN,
    base_url = config.BYPASS,
  )
  updater=Updater(
    bot=bot,
  )

  H_common=MessageHandler(Filters.all, commonMessage)
  H_tr=CommandHandler("tr", translateCall)
  H_reg=CommandHandler("reg", regCall)
  H_login=CommandHandler("login", loginCall)
  H_weather=CommandHandler("weather", weatherCall)
  H_help=CommandHandler("help", helpCall)
  H_exchange=CommandHandler("e", exchangeCall)
  H_test=CommandHandler("t", test)

  updater.dispatcher.add_handler(H_tr)
  updater.dispatcher.add_handler(H_reg)
  updater.dispatcher.add_handler(H_login)
  updater.dispatcher.add_handler(H_test)
  updater.dispatcher.add_handler(H_weather)
  updater.dispatcher.add_handler(H_help)
  updater.dispatcher.add_handler(H_exchange)
  updater.dispatcher.add_handler(H_common)
  
  updater.start_polling()
  updater.idle()


main()


# ['message_id', 'from_user', 'date', 'chat', 
# 'forward_from', 'forward_from_chat', 'forward_date', 
# 'reply_to_message', 'edit_date', 'text', 'entities', 
# 'caption_entities', 'audio', 'game', 'document', 'photo', 
# 'sticker', 'video', 'voice', 'video_note', 'caption', 'contact', 
# 'location', 'venue', 'new_chat_members', 'left_chat_member', 
# 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 
# 'group_chat_created', 'supergroup_chat_created', 'migrate_to_chat_id', 
# 'migrate_from_chat_id', 'channel_chat_created', 'pinned_message', 
# 'forward_from_message_id', 'invoice', 'successful_payment', 
# 'connected_website', 'forward_signature', 'author_signature', 
# 'media_group_id', 'animation', 'passport_data', 'bot', '_id_attrs', 
# '__module__', '__doc__', '_effective_attachment', 'ATTACHMENT_TYPES', 
# 'MESSAGE_TYPES', '__init__', 'chat_id', 'link', 'de_json', 
# 'effective_attachment', '__getitem__', 'to_dict', '_quote', 
# 'reply_text', 'reply_markdown', 'reply_html', 'reply_media_group', 
# 'reply_photo', 'reply_audio', 'reply_document', 'reply_animation', 
# 'reply_sticker', 'reply_video', 'reply_video_note', 'reply_voice', 
# 'reply_location', 'reply_venue', 'reply_contact', 'forward', 
# 'edit_text', 'edit_caption', 'edit_media', 'edit_reply_markup', 
# 'delete', 'parse_entity', 'parse_caption_entity', 'parse_entities', 
# 'parse_caption_entities', '_parse_html', 'text_html', 
# 'text_html_urled', 'caption_html', 'caption_html_urled', 
# '_parse_markdown', 'text_markdown', 'text_markdown_urled', 
# 'caption_markdown', 'caption_markdown_urled', '__metaclass__', 
# '__str__', 'to_json', '__eq__', '__hash__', '__dict__', 
# '__weakref__', '__repr__', '__getattribute__', '__setattr__', 
# '__delattr__', '__lt__', '__le__', '__ne__', '__gt__', '__ge__', 
# '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', 
# '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']


# {'id': 248678756, 'first_name': 'York', 'is_bot': False, 'username': 'YorkDW', 'language_code': 'ru'}