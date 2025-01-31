# Initializing our blockchain list
genesis_block = {
    'previous_hash': '', 
    'index': 0, 
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Yuriy'


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
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = str([last_block[key] for key in last_block])
    print(hashed_block)
    block = {
        'previous_hash': hashed_block, 
        'index': len(blockchain), 
        'transactions': open_transactions#[::]
    }
    blockchain.append(block)
    pass

    
def get_transaction_value():
    """ Returns the users input (a new transaction amount) as a float."""
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def verify():
    l = len(blockchain)
    if l < 2:
        return True#None
    i = l
    while i >= 2:
        current = blockchain[i-1]
        to_verify = blockchain[i-2]
        if current[0] == to_verify:
            i -= 1
        else:
            return False
    return True


def verify_chain():
    #block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            block_index += 1
            continue
        elif blockchain[block_index] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            #break    
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     if block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    return is_valid        
                

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)
            
            
waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: manipulate the chain')
    print('q: To end program')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block() 
    elif user_choice == '3':
        print_blockchain_elements()    
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    # if not verify_chain():
    #     print('Invalid blockchain!')
    #     break    
#    print(f'Choice registered! {verify()}')         
else:
    print('User left!')
    print('Here is blockchain we get:')
    print(*blockchain)    
    print('Done!')