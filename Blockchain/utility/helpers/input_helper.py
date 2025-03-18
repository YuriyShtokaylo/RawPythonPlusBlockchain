"""Common input functionality"""


from configs.consts import CHOICE_MSG, ASK_FOR_RECIPIENT_MSG, ASK_FOR_AMOUNT_MSG

"""Read user input"""


def get_user_choice():
    user_input = input(CHOICE_MSG)
    return user_input


"""Get transacton data provided by user"""


def get_transaction_value():
    """ Returns the users input (a new transaction amount) as a float."""
    tx_recipient = input(ASK_FOR_RECIPIENT_MSG)
    tx_amount = float(input(ASK_FOR_AMOUNT_MSG))
    return (tx_recipient, tx_amount)
