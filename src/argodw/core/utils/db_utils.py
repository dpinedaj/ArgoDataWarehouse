from typing import Union
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

def get_session(user: str, password: str, host: str, port: Union[str, int], db: str):
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}", echo=True)

    return scoped_session(
        sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False
        )
    )