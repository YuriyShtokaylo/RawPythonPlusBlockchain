# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """" Return the last value of the current blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    ''' Append a new value as well as the last blockchain to the blockchain
    
    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1])
    '''
    blockchain.append([last_transaction, transaction_amount])  


def get_transaction_value():
    """ Returns the users input (a new transaction amount) as a float."""
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


#Get first transaction input
tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    else:
        for block in blockchain:
            print('Outputting Block')
            print(block)
    
print('Done!')