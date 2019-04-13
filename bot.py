from api_keys import BOT_KEY


class telegram:

    def __init__(self):
        self.url = 'https://api.telegram.org/bot' + BOT_KEY


bot = telegram()

print(bot.url)
