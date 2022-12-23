from parsing import Bot
from bitrix import BitrixCrm, Deal

from time import sleep

def event(link):
    with Bot(link) as bot:
        bot.get_post_list()
        data = bot.get_data_for_bitrix()
    
    for i in data:
        deal = Deal(**i)
        bitrix = BitrixCrm(deal)
        try:
            bitrix.crm_add_deal()
        except Exception:
            pass


