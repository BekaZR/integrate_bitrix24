class Deal:
    TITLE = ''
    CURRENCY_ID = 'RUB'
    OPPORTUNITY = ''
    COMMENTS = ''
    ADDITIONAL_INFO = ''
    
    def __init__(self, title, opportunity, comments, additional_info):
        self.TITLE = title
        self.OPPORTUNITY = opportunity
        self.COMMENTS = comments
        self.ADDITIONAL_INFO = additional_info

    