from api_keys import BOT_KEY
import requests

class telegram:

    def __init__(self):
        self.name = 'RedTwitBot'
        self.aux = 'aux'
        self.url = 'https://api.telegram.org/bot' + BOT_KEY

    def get_me(self):
        http_response = requests.get(self.url+'/getMe')
        json_response = http_response.json()
        if json_response['ok']:
            return print('Bot is valid and working')
        else:
            return print('Bot error')

    def get_updates (self):
        # TODO
        self.aux = 'aux2'
        return True

    def get_last_chat_id_and_text(self):
        # TODO
        self.aux = 'aux3'
        return True

    def get_last_update_ip(self):
        # TODO
        self.aux = 'aux3'
        return True

    def send_message(self, message, chat_id):
        # TODO
        self.aux = 'aux3'
        new = message + chat_id
        print(new)
        return True



bot = telegram()
bot.get_me()\

