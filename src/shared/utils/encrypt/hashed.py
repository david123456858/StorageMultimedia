import hashlib

def hashing(input:str)-> str:
    return hashlib.sha256(input.lower().strip().encode()).hexdigest()

def verifyHashed(input:str,hash:str):
    hash_input = hashing(input)
    if (hash_input != hash):
        return False
    return True