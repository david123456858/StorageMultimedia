from sqlalchemy import Engine, create_engine
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional

load_dotenv()

TURSO_DATABASE_URL = os.environ.get('MY_SQL')
TURSO_DATABASE_TOKEN = os.environ.get('MY_TOKE_SQL')

class dataBaseTurso:
    _instance = None
    _engine: Optional[Engine] = None
    
    @classmethod
    def get_instance(cls) -> Engine:
        if cls._engine is None:
            cls._engine = create_engine(
                f"sqlite+{TURSO_DATABASE_URL}?secure=true",
                    connect_args={
                        "auth_token": TURSO_DATABASE_TOKEN
                    }
            )
        cls._instance = cls()
        return cls._engine      
    
Base = declarative_base()