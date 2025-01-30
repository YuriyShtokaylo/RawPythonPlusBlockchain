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


def get_user_input():
    """ Returns the users input (a new transaction amount) as a float."""
    return float(input('Your transaction amount please: '))

#Get first transaction input
tx_amount = get_user_input()
add_value(tx_amount)

#Get second transation
tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), 
          transaction_amount=tx_amount)

#...
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print('Chain')
print(blockchain)
for block in blockchain:
    print('Outputting Block')
    print(block)
    
print('Done!')