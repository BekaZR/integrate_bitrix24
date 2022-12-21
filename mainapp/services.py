from parsing.main import Bot, Parse


def event(link):
    bot = Bot(link)
    parse = Parse(bot())
    parse()
    data = parse.get_data_from_post()


