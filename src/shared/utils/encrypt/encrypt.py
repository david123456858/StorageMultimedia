from cryptography.fernet import Fernet
import hashlib
from dotenv import load_dotenv
import os
load_dotenv()
# Clave fija segura (cárgala desde .env o un archivo)
# key = Fernet.generate_key()  # Solo la primera vez
# print(key)
key = os.environ.get('KEY_ENCRYPT')

if key is None:
    raise ValueError('Error al cargar la clave de cifrado desde las variables de entorno')

cipher = Fernet(key.encode())

def encrypt(email: str) -> str:
    return cipher.encrypt(email.encode()).decode()

def decrypt(token: str) -> str:
    return cipher.decrypt(token.encode()).decode()