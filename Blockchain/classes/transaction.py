from collections import OrderedDict
from Helpers.consts import SENDER, RECIPIENT, AMOUNT


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __repr__(self):
        return str(self.__dict__)

    def to_ordered_dict(self):
        ordered_dict = OrderedDict(
            [(SENDER, self.sender), (RECIPIENT, self.recipient), (AMOUNT, self.amount)])
        return ordered_dict
