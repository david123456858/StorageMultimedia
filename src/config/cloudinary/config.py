from dotenv import load_dotenv
import os
import cloudinary

load_dotenv()


CLODINARY_NAME = os.environ.get('CLOUDINARY_NAME')
CLODINARY_KEY = os.environ.get('API_KEY_CLOUDINARY')
CLODINARY_SECRECT= os.environ.get('CLOUDINARY_SECRET')

config = cloudinary.config(
    cloud_name = CLODINARY_NAME, 
    api_key = CLODINARY_KEY, 
    api_secret = CLODINARY_SECRECT,
    secure=True
)
