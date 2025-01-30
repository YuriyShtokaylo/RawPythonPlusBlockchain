# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """" Return the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    ''' Append a new value as well as the last blockchain to the blockchain
    
    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1])
    '''
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])  


def get_transaction_value():
    """ Returns the users input (a new transaction amount) as a float."""
    user_input = float(input('Your transaction amount please: '))
    return user_input


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
        

while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: manipulate the chain')
    print('q: To end program')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        for block in blockchain:
            print('Outputting Block')
            print(block)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')
    print(f'Choice registered! {verify()}')         
print('Here is blockchain we get:')
print(*blockchain)    
print('Done!')