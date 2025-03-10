from collections import OrderedDict

from utility.classes.printable import Printable

from utility.consts import SENDER, RECIPIENT, AMOUNT


class Transaction(Printable):
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_ordered_dict(self):
        ordered_dict = OrderedDict(
            [(SENDER, self.sender), (RECIPIENT, self.recipient), (AMOUNT, self.amount)])
        return ordered_dict
