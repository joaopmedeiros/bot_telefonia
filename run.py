import telepot
from pprint import pprint
import time

bot = telepot.Bot('1028113865:AAFN6sioYEC8p0aNfkBiosVxmBoB6-GnE-U')
pprint(bot.getMe())

while True:
    bot.sendMessage(-375668005,'Testando 123')
    time.sleep(10)