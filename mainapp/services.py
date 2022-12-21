from parsing import Bot, Parse
from bitrix import BitrixCrm, Deal


def event(link):
    bot = Bot(link)
    parse = Parse(bot())
    parse()
    data = parse.get_data_from_post()
    for i in data:
        deal = Deal(**i)
        bitrix = BitrixCrm(deal)
        bitrix.crm_add_deal()


