import hashlib as hl
import json


def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    #EXPLANATION:
    #hashlib uses sha256 to generate hash in binary format
    #we pass there string generated from our dict by method of json library - dumps
    #we use encode on it to get corect encoding
    #we use hexdigest on result of heshing to get a string result
    return hash_string_256(json.dumps(block, sort_keys=True).encode())