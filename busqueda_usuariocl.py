import tweepy
from telegram import Bot

# Configuración de las credenciales de Twitter y Telegram
APP_KEY = 'MWnPKO1b8bHbezTRL5C9NHNbB'
APP_SECRET = 'z6vMI2uXI8lkEqEliV0hTNtituf1bq5ouXZiZrhEfPfm0RPFdB'
ACCESS_TOKEN = '1567899448381939713-oDeheDx7kO1ETmHtTVNj42MXKe16hs'
ACCESS_TOKEN_SECRET = 'jOaapnHDEjXH5sUgOYP54PjqzegzaZfqSCct88BlO1jAY'
TWITTER_USER_IDS = ['1567899448381939713']  # Agrega aquí los identificadores de los usuarios de Twitter
TELEGRAM_TOKEN = 'AAHGQGznxgjdh3FuaaRwaCi0y8Sy1wBrEhA'
TELEGRAM_CHAT_IDS = ['@decimo_executor']  # Agrega aquí los identificadores de los chats de Telegram

# Configurar la autenticación de Twitter
auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Crear una instancia de StreamListener personalizado
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweet_text = status.text
        tweet_id = status.id_str
        tweet_url = f'https://twitter.com/user/status/{tweet_id}'
        send_telegram_message(tweet_text, tweet_url)

    def on_error(self, status_code):
        print('Error:', status_code)
# Función para enviar mensaje a Telegram
def send_telegram_message(tweet_text, tweet_url):
    for chat_id in TELEGRAM_CHAT_IDS:
        message = f'{tweet_text}\n\n{tweet_url}'
        bot.send_message(chat_id=chat_id, text=message)

        print(f'Mensaje enviado a chat {chat_id}')

# Iniciar el streaming y escuchar los tweets en tiempo real
def start_twitter_stream():
    my_listener = MyStreamListener(auth=api.auth)
    my_listener.filter(follow=TWITTER_USER_IDS)

# Iniciar el escaneo de los timelines de Twitter
start_twitter_stream()
