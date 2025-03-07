from classes.verification import Verification

from Helpers.consts import GENESIS_BLOCK, SENDER, RECIPIENT, AMOUNT, SYSTEM_ACCOUNT, MINING_REWARD, PREVIOUS_HASH, INDEX, TRANSACTIONS, PROOF, ASK_MSG, O1_MSG, O2_MSG, O3_MSG, O4_MSG, O5_MSG, O6_MSG, O7_MSG, O_BLOCK_MSG, S_T_MSG, F_MSG, F_T_MSG, E_MSG, Q_MSG, R_MSG
from Helpers.input_helper import get_user_choice, get_transaction_value


class Node:
    def print_blockchain_elements(self, blockchain):
        for block in blockchain:
            print(O_BLOCK_MSG)
            print(block)
        else:
            print('-' * 20)

    def listen_for_input(self, participants, owner, blockchain, open_transactions, add_transaction, mine_block, save_data, get_balance):
        waiting_for_input = True

        while waiting_for_input:
            print(ASK_MSG)
            print(O1_MSG)
            print(O2_MSG)
            print(O3_MSG)
            print(O4_MSG)
            print(O6_MSG)
            user_choice = get_user_choice()
            verifier = Verification()
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
                self.print_blockchain_elements(blockchain)
            elif user_choice == '4':
                print(participants)
                if verifier.verify_transactions(open_transactions, get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print(O7_MSG)
            if not verifier.verify_chain(blockchain):
                print(E_MSG)
                break
            print('Balance of {}: {:6.2f}'.format(owner, get_balance(owner)))
        else:
            print(Q_MSG)
            print(R_MSG)
            print(F_MSG)
