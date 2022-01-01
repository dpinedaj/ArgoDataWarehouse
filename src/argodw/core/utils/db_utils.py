import os
from contextlib import contextmanager
from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker

@contextmanager
def get_session():
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    db = os.environ['POSTGRES_DB']
    host = os.environ['POSTGRES_HOST']
    port = os.environ['POSTGRES_PORT']

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}", echo=True)

    session = scoped_session(
        sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False
        )
    )
    yield session

    session.close()
    