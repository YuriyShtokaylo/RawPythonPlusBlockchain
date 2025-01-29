'''
def greet():
    greeting = 'Hello'
    greeting += ' World!'
    print(greeting)


greet()
'''

blockchain = [1]

def add_value():
    blockchain.append([blockchain[-1], 5.3])
    print(blockchain)    


add_value()
add_value()
add_value()