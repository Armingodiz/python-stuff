import telebot
import time


bot_token = "1273130948:AAF78YNbkiT_gILq7FFnU6lgnRFJwWPLfjo"


bot = telebot.TeleBot(token= bot_token)


def find_at(msg):
	for text in msg :
		if '@' in text :
			return text


@bot.message_handler(commands = ['start'])
def send_welcome(message):
	bot.reply_to(message , ' welcom to my bot press \help for more info')

@bot.message_handler(commands=['help'])
def help_user(message):
	bot.reply_to(message , 'list of commands : \Doller \n \Gold  \n \aboutMe ')
 

@bot.message_handler(func= lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
	texts = message.text.split()
	at_text = find_at(texts)
	bot.reply_to(message, 'http://instagram.com/{}'.format(at_text[1:]))

@bot.message_handler(commands = ['Doller'])
def send_welcome(message):
	bot.reply_to(message , ' Doller is '++" RIAL right now ")


@bot.message_handler(commands = ['Gold'])
def send_welcome(message):
	bot.reply_to(message , ' welcom to my bot press \help for more info')



@bot.message_handler(commands = ['aboutMe'])
def send_welcome(message):
	bot.reply_to(message , ' welcom to my bot press \help for more info')


while True:
	try:
		bot.polling()
	except Exception:
		break
