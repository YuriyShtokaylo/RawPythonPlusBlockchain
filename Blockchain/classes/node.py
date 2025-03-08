from uuid import uuid4

from classes.verification import Verification
from classes.blockchain import Blockchain

from Helpers.consts import OWNER, ASK_MSG, O1_MSG, O2_MSG, O3_MSG, O4_MSG, O6_MSG, O7_MSG, O_BLOCK_MSG, S_T_MSG, F_MSG, F_T_MSG, E_MSG, Q_MSG, R_MSG
from Helpers.input_helper import get_user_choice, get_transaction_value


class Node:
    def __init__(self):
        # self.id = str(uuid4())
        self.id = OWNER
        self.blockchain = Blockchain(self.id)
        pass

    def print_blockchain_elements(self):
        for block in self.blockchain.get_chain():
            print(O_BLOCK_MSG)
            print(block)
        else:
            print('-' * 20)

    def listen_for_input(self):
        waiting_for_input = True

        while waiting_for_input:
            print(ASK_MSG)
            print(O1_MSG)
            print(O2_MSG)
            print(O3_MSG)
            print(O4_MSG)
            print(O6_MSG)
            user_choice = get_user_choice()
            if user_choice == '1':
                tx_data = get_transaction_value()
                recipient, amount = tx_data
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print(S_T_MSG)
                else:
                    print(F_T_MSG)
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print(O7_MSG)
            if not Verification.verify_chain(self.blockchain.get_chain()):
                print(E_MSG)
                break
            print('Balance of {}: {:6.2f}'.format(
                self.id, self.blockchain.get_balance()))
        else:
            print(Q_MSG)
            print(R_MSG)
            print(F_MSG)
