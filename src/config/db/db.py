from sqlalchemy import Engine, create_engine, text
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional
import logging

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
        cls._sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind= cls._engine)
        cls._instance = cls()
        return cls._engine      

    @classmethod
    def test_connection(cls):
        try:
            engine= cls.get_instance()
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
                print('✅ Conexión a la base de datos exitosa.') 
                return True
        except Exception as error:
            logging.error(f"❌ Error de conexión a la base de datos: {error}")
            return False
            
Base = declarative_base()