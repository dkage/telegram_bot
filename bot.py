from api_keys import BOT_KEY
import requests


class Telegram:

    def __init__(self):
        self.name = ''
        self.url = "https://api.telegram.org/bot{}/".format(BOT_KEY)
        self.bot_id = 0
        self.offset = None

    def get_me(self):
        http_response = requests.get(self.url+'getMe')
        json_response = http_response.json()
        self.bot_id = json_response['result']['id']
        self.name = json_response['result']['username']
        if json_response['ok']:
            return True
        else:
            return False

    def get_updates(self):
        update_url = self.url + 'getUpdates?timeout=100'
        if self.offset:
            update_url += "&offset={}".format(self.offset)
        http_response = requests.get(update_url)
        json_response = http_response.json()
        print(update_url)
        print(json_response)
        # TODO get highest JSON element to get latest message_id/update_id
        self.offset = json_response['result'][-1]['update_id']
        if json_response['ok']:
            return json_response['result']
        else:
            return False

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


bot = Telegram()
bot.get_me()
print('update 1')
bot.get_updates()
print('update 2')
bot.get_updates()
