from cryptography.fernet import Fernet
import hashlib

# Clave fija segura (cárgala desde .env o un archivo)
key = Fernet.generate_key()  # Solo la primera vez
print(key)
cipher = Fernet(key)

def encrypt(email: str) -> str:
    return cipher.encrypt(email.encode()).decode()

def decrypt(token: str) -> str:
    return cipher.decrypt(token.encode()).decode()