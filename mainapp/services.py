from parsing import Bot
from bitrix import BitrixCrm, Deal


def event(link):
    with Bot(link) as bot:
        bot.get_post_list()
        data = bot.get_data_for_bitrix()
    
    for i in data:
        deal = Deal(**i)
        bitrix = BitrixCrm(deal)
        bitrix.crm_add_deal()


