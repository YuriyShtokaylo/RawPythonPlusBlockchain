"""Common hashing functionality"""


import hashlib as hl
import json

__all__ = ['hash_string_256', 'hash_block']

from configs.consts import TRANSACTIONS


def hash_string_256(string):
    """Creates a SHA256 hash for a given input string.
    
    Arguments:
        :string: The string which should be hashed.
    """
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """Hashes a block and returns a string representation of it.
    
    Arguments:
        :block: The block that should be hashed.
    """
    hashable_block = block.__dict__.copy()
    hashable_block[TRANSACTIONS] = [tx.to_ordered_dict()
                                    for tx in hashable_block[TRANSACTIONS]]
    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())
