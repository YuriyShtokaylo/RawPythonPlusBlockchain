from time import time

from utility.classes.printable import Printable

from configs.consts import TRANSACTIONS


class Block(Printable):
    def __init__(self, index, previous_hash, transactions, proof, time=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof

    def do_saveable(self):
        saveable = self.__dict__.copy()
        saveable_transactions = [
            tx.__dict__ for tx in self.transactions.copy()]
        saveable[TRANSACTIONS] = saveable_transactions
        return saveable
