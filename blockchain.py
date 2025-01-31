MINING_REWARD = 10
SYSTEM_ACCOUNT = 'MINING'

sender_const = 'sender'
recipient_const = 'recipient'
amount_const = 'amount'
previous_hash_const = 'previous_hash'
index_const = 'index'
transactions_const = 'transactions'


ask_for_recipient_msg = 'Enter the recipient of the transaction: '
ask_for_amount_msg = 'Your transaction amount please: '
choice_msg = 'Your choice: '
o_block_msg = 'Outputting Block'
ask_msg = 'Please choose'
o1_msg = '1: Add a new transaction value'
o2_msg = '2: Mine a new block'
o3_msg = '3: Output the blockchain blocks'
o4_msg = '4: Output participants'
o5_msg = 'h: manipulate the chain'
o6_msg = 'q: To end program'
o7_msg = 'Input was invalid, please pick a value from the list!'
e_msg = 'Invalid blockchain!'
q_msg = 'User left!'
r_msg = 'Here is blockchain we get:'
f_msg = 'Done!'


genesis_block = {
    'previous_hash': '', 
    'index': 0, 
    'transactions': []
}


# Initializing our blockchain list
blockchain = [genesis_block]
open_transactions = []
owner = 'Yuriy'
participants = {owner}


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
    transaction = {
        sender_const: sender, 
        recipient_const: recipient, 
        amount_const: amount
    }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        sender_const: SYSTEM_ACCOUNT,
        recipient_const: owner,
        amount_const: MINING_REWARD
    }
    open_transactions.append(reward_transaction)
    block = {
        previous_hash_const: hashed_block, 
        index_const: len(blockchain), 
        transactions_const: open_transactions
    }
    blockchain.append(block)
    return True

    
def get_transaction_value():
    """ Returns the users input (a new transaction amount) as a float."""
    tx_recipient = input(ask_for_recipient_msg)
    tx_amount = float(input(ask_for_amount_msg))
    return (tx_recipient, tx_amount)


def get_user_choice():
    user_input = input(choice_msg)
    return user_input


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block[previous_hash_const] != hash_block(blockchain[index - 1]):
            return False    
    return True       


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx[amount_const] for tx in block[transactions_const] if tx[sender_const] == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender[1:]:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx[amount_const] for tx in block[transactions_const] if tx[recipient_const] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient[1:]:
        if len(tx) > 0:
            amount_received += tx[0]        
    return amount_received - amount_sent
                    

def print_blockchain_elements():
    for block in blockchain:
        print(o_block_msg)
        print(block)
    else:
        print('-' * 20)
            
            
waiting_for_input = True

while waiting_for_input:
    print(ask_msg)
    print(o1_msg)
    print(o2_msg)
    print(o3_msg)
    print(o4_msg)
    print(o5_msg)
    print(o6_msg)
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
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
                previous_hash_const: '', 
                index_const: 0, 
                transactions_const: [{sender_const: 'Wrong', recipient_const: 'WrongWrongWrong', amount_const: -1}]  
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print(o7_msg)
    if not verify_chain():
        print(e_msg)
        break   
    print(get_balance(owner))         
else:
    print(q_msg)
    print(r_msg)
    print(*blockchain)    
    print(f_msg)