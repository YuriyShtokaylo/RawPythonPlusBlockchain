from collections import OrderedDict

from utility.classes.printable import Printable

from configs.consts import SENDER, RECIPIENT, AMOUNT


class Transaction(Printable):
    """A transaction which can be added to a block in the blockchain.
    
    Attribute:
        :sender: The sender of coins.
        :recipient: The recipient of the coins.
        :signature: The signature of the transaction.
        :amount: The amount of coins sent.
    """
    def __init__(self, sender, recipient, signature, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    def to_ordered_dict(self):
        ordered_dict = OrderedDict(
            [(SENDER, self.sender), (RECIPIENT, self.recipient), (AMOUNT, self.amount)])
        return ordered_dict
