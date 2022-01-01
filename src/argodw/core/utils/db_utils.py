import os
from contextlib import contextmanager
from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker

@contextmanager
def get_session():
    user = 'admin' #os.environ['POSTGRES_USER']
    password = 'admin' #os.environ['POSTGRES_PASSWORD']
    db = 'pruebas' #os.environ['POSTGRES_DB']
    host = 'localhost' #os.environ['POSTGRES_HOST']
    port = 5432 #os.environ['POSTGRES_PORT']

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}", echo=True)

    session = scoped_session(
        sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False
        )
    )
    yield session, engine

    session.close()
    