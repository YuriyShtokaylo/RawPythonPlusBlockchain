import hashlib as hl


def valid_proof(transactions, last_hash, proof):
    guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) + str(proof)).encode()
    guess_hash =hl.sha256(guess).hexdigest()
    return guess_hash[0:2] == '00'