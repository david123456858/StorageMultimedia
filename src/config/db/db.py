from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()


DATA_BASE = f'{os.getenv('MY_SQL')}?authToken={os.getenv('MY_TOKE_SQL')}'
print(DATA_BASE)
engine = create_engine(DATA_BASE)
localSession = sessionmaker(autocommit=True, autoflush=True, bind=engine)
Base = declarative_base() 

try:
    with engine.connect() as connection:
        print('Se conecto')
except:
    print('❌ No se conecto')
    
