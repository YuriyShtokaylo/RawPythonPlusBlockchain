from functools import reduce
import json

from classes.block import Block
from classes.transaction import Transaction
from classes.verification import Verification
from classes.node import Node

from Helpers.consts import GENESIS_BLOCK, SENDER, RECIPIENT, AMOUNT, SYSTEM_ACCOUNT, MINING_REWARD, PREVIOUS_HASH, INDEX, TRANSACTIONS, PROOF, ASK_MSG, O1_MSG, O2_MSG, O3_MSG, O4_MSG, O5_MSG, O6_MSG, O7_MSG, O_BLOCK_MSG, S_T_MSG, F_MSG, F_T_MSG, E_MSG, Q_MSG, R_MSG
from Helpers.hash_helper import hash_block
from Helpers.input_helper import get_user_choice, get_transaction_value


# Initializing our blockchain list
blockchain = [GENESIS_BLOCK]
open_transactions = []
owner = 'Yuriy'
participants = {owner}


def save_data():
    try:
        with open('blockchain.txt', mode='w') as f:
            saveable_chain = [block.do_saveable() for block in blockchain]
            f.write(json.dumps(saveable_chain))
            f.write('\n')
            saveable_transactions = [tx.__dict__ for tx in open_transactions]
            f.write(json.dumps(saveable_transactions))
        '''
        with open('blockchain.txt', mode='wb') as f: #Work with binary
            save_data = {
                'chain': blockchain,
                'ot': open_transactions
            }
            f.write(pickle.dumps(save_data))
        '''
    except (IOError, IndexError):
        print('Saving failed!')


def load_data():
    global blockchain
    global open_transactions
    '''
    with open('blockchain.txt', mode='rb') as f:
        file_content = pickle.loads(f.read())
        print(file_content)
        global blockchain
        global open_transactions
        blockchain = file_content['chain']
        open_transactions = file_content['ot']
    '''
    try:
        with open('blockchain.txt', mode='r') as f:
            file_content = f.readlines()
            blockchain = json.loads(file_content[0][:-1])
            updated_blockchain = []
            for block in blockchain:
                converted_tx = [Transaction(
                    tx[SENDER], tx[RECIPIENT], tx[AMOUNT]) for tx in block[TRANSACTIONS]]
                updated_block = Block(
                    block[INDEX], block[PREVIOUS_HASH], converted_tx, block[PROOF], block['timestamp'])
                updated_blockchain.append(updated_block)
            blockchain = updated_blockchain
            open_transactions = [Transaction(
                tx[SENDER], tx[RECIPIENT], tx[AMOUNT]) for tx in json.loads(file_content[1])]
    except IOError:
        blockchain = [GENESIS_BLOCK]
        open_transactions = []

load_data()


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    verifier = Verification()
    while not verifier.valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_last_blockchain_value():
    """" Return the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    ''' Append a new value as well as the last blockchain to the blockchain

    Arguments:
        :sender: Transaction sender.
        :recipient: Transaction recipient (default [1])
        :amount: Transaction amount (default 1.0 coin)
    '''
    transaction = Transaction(sender, recipient, amount)
    verifier = Verification()
    if verifier.verify_transaction(transaction, get_balance):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        save_data()
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    reward_transaction = Transaction(SYSTEM_ACCOUNT, owner, MINING_REWARD)
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = Block(len(blockchain), hashed_block, copied_transactions, proof)
    blockchain.append(block)
    return True


def get_balance(participant):
    tx_sender = [[tx.amount for tx in block.transactions if tx.sender
                  == participant] for block in blockchain]
    open_tx_sender = [tx.amount
                      for tx in open_transactions if tx.sender == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                         if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient
                     == participant] for block in blockchain]
    amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                             if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
    return amount_received - amount_sent


def print_blockchain_elements():
    for block in blockchain:
        print(O_BLOCK_MSG)
        print(block)
    else:
        print('-' * 20)


# waiting_for_input = True

node = Node()
node.listen_for_input(participants, owner, blockchain, open_transactions, add_transaction, mine_block, save_data, print_blockchain_elements, get_balance)

# while waiting_for_input:
#     print(ASK_MSG)
#     print(O1_MSG)
#     print(O2_MSG)
#     print(O3_MSG)
#     print(O4_MSG)
#     print(O6_MSG)
#     user_choice = get_user_choice()
#     verifier = Verification()
#     if user_choice == '1':
#         tx_data = get_transaction_value()
#         recipient, amount = tx_data
#         if add_transaction(recipient, amount=amount):
#             print(S_T_MSG)
#         else:
#             print(F_T_MSG)
#     elif user_choice == '2':
#         if mine_block():
#             open_transactions = []
#             save_data()
#     elif user_choice == '3':
#         print_blockchain_elements()
#     elif user_choice == '4':
#         print(participants)
#         if verifier.verify_transactions(open_transactions, get_balance):
#             print('All transactions are valid')
#         else:
#             print('There are invalid transactions')    
#     elif user_choice == 'q':
#         waiting_for_input = False
#     else:
#         print(O7_MSG)
#     if not verifier.verify_chain(blockchain):
#         print(E_MSG)
#         break
#     print('Balance of {}: {:6.2f}'.format(owner, get_balance(owner)))
# else:
#     print(Q_MSG)
#     print(R_MSG)
#     print(F_MSG)
