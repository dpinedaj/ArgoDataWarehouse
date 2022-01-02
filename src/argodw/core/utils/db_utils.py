import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


@contextmanager
def get_session():
    user = 'postgres'
    password = 'password'
    db = 'postgres'
    host = 'postgres'
    port = 5432

    engine = create_engine(
        f"postgresql://{user}:{password}@{host}:{port}/{db}", echo=True)

    session = scoped_session(
        sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False
        )
    )
    yield session, engine

    session.close()
