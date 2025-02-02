import functools

MINING_REWARD = 10
SYSTEM_ACCOUNT = 'MINING'

SENDER = 'sender'
RECIPIENT = 'recipient'
AMOUNT = 'amount'
PREVIOUS_HASH = 'previous_hash'
INDEX = 'index'
TRANSACTIONS = 'transactions'


ASK_FOR_RECIPIENT_MSG = 'Enter the recipient of the transaction: '
ASK_FOR_AMOUNT_MSG = 'Your transaction amount please: '
CHOICE_MSG = 'Your choice: '
O_BLOCK_MSG = 'Outputting Block'
ASK_MSG = 'Please choose'
O1_MSG = '1: Add a new transaction value'
O2_MSG = '2: Mine a new block'
O3_MSG = '3: Output the blockchain blocks'
O4_MSG = '4: Output participants'
O5_MSG = 'h: manipulate the chain'
O6_MSG = 'q: To end program'
O7_MSG = 'Input was invalid, please pick a value from the list!'
E_MSG = 'Invalid blockchain!'
Q_MSG = 'User left!'
R_MSG = 'Here is blockchain we get:'
F_MSG = 'Done!'
S_T_MSG = 'Added transaction!'
F_T_MSG = 'Transaction failed!'


GENESIS_BLOCK = {
    PREVIOUS_HASH: '', 
    INDEX: 0, 
    TRANSACTIONS: []
}


# Initializing our blockchain list
blockchain = [GENESIS_BLOCK]
open_transactions = []
owner = 'Yuriy'
participants = {owner}


def get_last_blockchain_value():
    """" Return the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction[SENDER])
    return sender_balance >= transaction[AMOUNT]


def add_transaction(recipient, sender=owner, amount=1.0):
    ''' Append a new value as well as the last blockchain to the blockchain
    
    Arguments:
        :sender: Transaction sender.
        :recipient: Transaction recipient (default [1])
        :amount: Transaction amount (default 1.0 coin)
    '''
    transaction = {
        SENDER: sender, 
        RECIPIENT: recipient, 
        AMOUNT: amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        SENDER: SYSTEM_ACCOUNT,
        RECIPIENT: owner,
        AMOUNT: MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        PREVIOUS_HASH: hashed_block, 
        INDEX: len(blockchain), 
        TRANSACTIONS: copied_transactions
    }
    blockchain.append(block)
    return True

    
def get_transaction_value():
    """ Returns the users input (a new transaction amount) as a float."""
    tx_recipient = input(ASK_FOR_RECIPIENT_MSG)
    tx_amount = float(input(ASK_FOR_AMOUNT_MSG))
    return (tx_recipient, tx_amount)


def get_user_choice():
    user_input = input(CHOICE_MSG)
    return user_input


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block[PREVIOUS_HASH] != hash_block(blockchain[index - 1]):
            return False    
    return True       


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx[AMOUNT] for tx in block[TRANSACTIONS] if tx[SENDER] == participant] for block in blockchain]
    open_tx_sender = [tx[AMOUNT] for tx in open_transactions if tx[SENDER] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + tx_amt[0] if len(tx_amt) > 0 else 0, tx_sender, 0)
    tx_recipient = [[tx[AMOUNT] for tx in block[TRANSACTIONS] if tx[RECIPIENT] == participant] for block in blockchain]
    amount_received = functools.reduce(lambda tx_sum, tx_amt: tx_sum + tx_amt[0] if len(tx_amt) > 0 else 0, tx_recipient, 0)   
    return amount_received - amount_sent
                    

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
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = [] 
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
    print(*blockchain)    
    print(F_MSG)