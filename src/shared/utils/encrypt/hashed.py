import bcrypt
import hashlib

def hashing(input:str)-> str:
    return bcrypt.hashpw(input.encode(), bcrypt.gensalt()).decode()

def verify_password(input_password: str, stored_hash: str) -> bool:
    return bcrypt.checkpw(input_password.encode(), stored_hash.encode())

def hashing_hashlib (input:str):
    return hashlib.sha256(input.encode()).hexdigest()
