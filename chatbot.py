from telegram.ext import Updater
from telegram.ext import CommandHandler
from config import Configuration
from db import DBConnection,Query
import datetime
import json

token = Configuration.get_token('telegram')
 
BOT_TOKEN=token[1]
 
updater = Updater( token=BOT_TOKEN, use_context=True )
dispatcher = updater.dispatcher

def db_access():
    configuration = Configuration.get_configuration('local')
    _host = configuration['host']
    _user = configuration['user']
    _password = configuration['password']
    _database = configuration['database']
    _port = configuration['port']
    _charset = configuration['charset']

    conn = DBConnection(host=_host,
            user=_user,
            password=_password,
            database=_database,
            port=_port,
            charset=_charset)
    return conn
 
def howto(update, context):
	text = '[사용방법]\n실시간 뉴스정보 /news\n실시간 과제공고 /rnd'
	context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def news(update, context):

	try:

		conn = db_access()
		data = conn.exec_select(2)
		conn.close()

		prefix = '뉴스'
		title = data[0]['title']
		thumbnail = data[0]['thumbnail']
		summary = data[0]['summary']
		rdate = data[0]['rdate']
		link = data[0]['link']
		text = '{}\n{}\n{}\n{}\n{}\n{}'.format(prefix,thumbnail,title,summary,rdate,link)

		context.bot.send_message(chat_id=update.effective_chat.id, text=text)

	except Exception as e:
		with open('./error.log','a') as file:
			file.write('{} You got an error: {}\n'.format(datetime.datetime.now().strtime('%Y-%m-%d %H:%M:%S'),str(e)))

def rnd(update, context):

	try:


		conn = db_access()
		data = conn.exec_select(1)
		conn.close()

		prefix = '과제공고'
		goverment = data[0]['goverment']
		title = data[0]['title']
		period = data[0]['period']
		posted = data[0]['posted']
		link = data[0]['link']
		text = '{}\n{}\n{}\n{}\n{}\n{}'.format(prefix,goverment,title,period,posted,link)

		context.bot.send_message(chat_id=update.effective_chat.id, text=text)

	except Exception as e:
		with open('./error.log','a') as file:
			file.write('{} You got an error: {}\n'.format(datetime.datetime.now().strtime('%Y-%m-%d %H:%M:%S'),str(e)))
 
howto_handler = CommandHandler('howto', howto)
news_handler = CommandHandler('news', news)
rnd_handler = CommandHandler('rnd', rnd)
 
dispatcher.add_handler(howto_handler)
dispatcher.add_handler(news_handler)
dispatcher.add_handler(rnd_handler)
 
updater.start_polling()
updater.idle()