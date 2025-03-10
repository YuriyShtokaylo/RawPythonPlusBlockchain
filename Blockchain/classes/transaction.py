from collections import OrderedDict
from Helpers.consts import SENDER, RECIPIENT, AMOUNT
from classes.printable import Printable


class Transaction(Printable):
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_ordered_dict(self):
        ordered_dict = OrderedDict(
            [(SENDER, self.sender), (RECIPIENT, self.recipient), (AMOUNT, self.amount)])
        return ordered_dict
