from functools import reduce
import json

from classes.block import Block
from classes.transaction import Transaction
from classes.verification import Verification

from Helpers.consts import GENESIS_BLOCK, SENDER, RECIPIENT, AMOUNT, SYSTEM_ACCOUNT, MINING_REWARD, PREVIOUS_HASH, INDEX, TRANSACTIONS, PROOF
from Helpers.hash_helper import hash_block


class Blockchain:

    def __init__(self, node_id):
        # Initializing our blockchain list
        self.chain = [GENESIS_BLOCK]
        self.open_transactions = []
        self.hosting_node = node_id
        self.load_data()

    def save_data(self):
        try:
            with open('blockchain.txt', mode='w') as f:
                saveable_chain = [block.do_saveable() for block in self.chain]
                f.write(json.dumps(saveable_chain))
                f.write('\n')
                saveable_transactions = [
                    tx.__dict__ for tx in self.open_transactions]
                f.write(json.dumps(saveable_transactions))
        except (IOError, IndexError):
            print('Saving failed!')

    def load_data(self):
        try:
            with open('blockchain.txt', mode='r') as f:
                file_content = f.readlines()
                self.chain = json.loads(file_content[0][:-1])
                updated_blockchain = []
                for block in self.chain:
                    converted_tx = [Transaction(
                        tx[SENDER], tx[RECIPIENT], tx[AMOUNT]) for tx in block[TRANSACTIONS]]
                    updated_block = Block(
                        block[INDEX], block[PREVIOUS_HASH], converted_tx, block[PROOF], block['timestamp'])
                    updated_blockchain.append(updated_block)
                self.chain = updated_blockchain
                self.open_transactions = [Transaction(
                    tx[SENDER], tx[RECIPIENT], tx[AMOUNT]) for tx in json.loads(file_content[1])]
        except IOError:
            print('Handled exception...')
        finally:
            print('Cleanup!')

    def proof_of_work(self):
        last_block = self.chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        verifier = Verification()
        while not verifier.valid_proof(self.open_transactions, last_hash, proof):
            proof += 1
        return proof

    def get_last_blockchain_value(self):
        """" Return the last value of the current blockchain """
        if len(self.chain) < 1:
            return None
        return self.chain[-1]

    def add_transaction(self, recipient, sender, amount=1.0):
        ''' Append a new value as well as the last blockchain to the blockchain

        Arguments:
            :sender: Transaction sender.
            :recipient: Transaction recipient
            :amount: Transaction amount (default 1.0 coin)
        '''
        transaction = Transaction(sender, recipient, amount)
        verifier = Verification()
        if verifier.verify_transaction(transaction, self.get_balance):
            self.open_transactions.append(transaction)
            self.save_data()
            return True
        return False

    def mine_block(self):
        last_block = self.chain[-1]
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()
        reward_transaction = Transaction(
            SYSTEM_ACCOUNT, self.hosting_node, MINING_REWARD)
        copied_transactions = self.open_transactions[:]
        copied_transactions.append(reward_transaction)
        block = Block(len(self.chain), hashed_block,
                      copied_transactions, proof)
        self.chain.append(block)
        self.open_transactions = []
        self.save_data()
        return True

    def get_balance(self):
        participant = self.hosting_node
        tx_sender = [[tx.amount for tx in block.transactions if tx.sender
                      == participant] for block in self.chain]
        open_tx_sender = [tx.amount
                          for tx in self.open_transactions if tx.sender == participant]
        tx_sender.append(open_tx_sender)
        amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                             if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
        tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient
                        == participant] for block in self.chain]
        amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                                 if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
        return amount_received - amount_sent
