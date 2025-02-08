from functools import reduce
import hashlib as hl
from collections import OrderedDict
import json
import pickle


from Helpers.consts import GENESIS_BLOCK, SENDER, RECIPIENT, AMOUNT, SYSTEM_ACCOUNT, MINING_REWARD, PREVIOUS_HASH, INDEX, TRANSACTIONS, PROOF, ASK_MSG, O1_MSG, O2_MSG, O3_MSG, O4_MSG, O5_MSG, O6_MSG, O7_MSG, O_BLOCK_MSG, S_T_MSG, F_MSG, F_T_MSG, E_MSG, Q_MSG, R_MSG
from Helpers.hash_helper import hash_string_256, hash_block
from Helpers.input_helper import get_user_choice, get_transaction_value
from Helpers.proof_helper import valid_proof


# Initializing our blockchain list
blockchain = [GENESIS_BLOCK]
open_transactions = []
owner = 'Yuriy'
participants = {owner}


def save_data():
    try:
        with open('blockchain.txt', mode='w') as f:
            f.write(json.dumps(blockchain))
            f.write('\n')
            f.write(json.dumps(open_transactions))
        '''
        with open('blockchain.txt', mode='wb') as f: #Work with binary
            save_data = {
                'chain': blockchain,
                'ot': open_transactions
            }
            f.write(pickle.dumps(save_data))
        '''
    except IOError:
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
                updated_block = block.copy()
                updated_block[TRANSACTIONS] = [ OrderedDict( [(k, v) for k, v in transaction.items()] ) for transaction in block[TRANSACTIONS] ] 
                updated_blockchain.append(updated_block)
            blockchain = updated_blockchain
            open_transactions = [OrderedDict([(k, v) for k, v in d.items()]) for d in json.loads(file_content[1])]
    except IOError:
        blockchain = [GENESIS_BLOCK]
        open_transactions = []
        
            
    load_data()


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
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
    transaction = OrderedDict([
        (SENDER, sender), 
         (RECIPIENT, recipient), 
         (AMOUNT, amount)
        ])
    if verify_transaction(transaction):
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
    reward_transaction = OrderedDict([
        (SENDER, SYSTEM_ACCOUNT),
        (RECIPIENT, owner),
        (AMOUNT, MINING_REWARD)
    ])
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        PREVIOUS_HASH: hashed_block, 
        INDEX: len(blockchain), 
        TRANSACTIONS: copied_transactions,
        PROOF: proof
    }
    blockchain.append(block)
    return True


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block[PREVIOUS_HASH] != hash_block(blockchain[index - 1]):
            return False    
        if not valid_proof(block[TRANSACTIONS][:-1], block[PREVIOUS_HASH], block[PROOF]):
            print('Proof of work is invalid')
            return False
    return True       


def get_balance(participant):
    tx_sender = [[tx[AMOUNT] for tx in block[TRANSACTIONS] if tx[SENDER] == participant] for block in blockchain]
    open_tx_sender = [tx[AMOUNT] for tx in open_transactions if tx[SENDER] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    tx_recipient = [[tx[AMOUNT] for tx in block[TRANSACTIONS] if tx[RECIPIENT] == participant] for block in blockchain]
    amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)   
    return amount_received - amount_sent


def verify_transaction(transaction):
    sender_balance = get_balance(transaction[SENDER])
    return sender_balance >= transaction[AMOUNT]
                    

def print_blockchain_elements():
    for block in blockchain:
        print(O_BLOCK_MSG)
        print(block)
    else:
        print('-' * 20)
            
            
waiting_for_input = True

while waiting_for_input:
    print(ASK_MSG)
    print(O1_MSG)
    print(O2_MSG)
    print(O3_MSG)
    print(O4_MSG)
    print(O5_MSG)
    print(O6_MSG)
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print(S_T_MSG)
        else:
            print(F_T_MSG)    
    elif user_choice == '2':
        if mine_block():
            open_transactions = [] 
            save_data()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)    
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                PREVIOUS_HASH: '', 
                INDEX: 0, 
                TRANSACTIONS: [{SENDER: 'Wrong', RECIPIENT: 'WrongWrongWrong', AMOUNT: -1}]  
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print(O7_MSG)
    if not verify_chain():
        print(E_MSG)
        break   
    print('Balance of {}: {:6.2f}'.format(owner, get_balance(owner)))         
else:
    print(Q_MSG)
    print(R_MSG)  
    print(F_MSG)