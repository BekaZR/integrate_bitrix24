from fast_bitrix24 import Bitrix

from core.settings import BITRIX_URL

webhook = BITRIX_URL

b = Bitrix(webhook)

class BitrixCrm:
    method = 'crm.deal.add'

    def __init__(self, deal):
        self.deal = deal

    def crm_add_deal(self):
        params = {'fields': self.deal.__dict__}
        b.call(self.method, params)
