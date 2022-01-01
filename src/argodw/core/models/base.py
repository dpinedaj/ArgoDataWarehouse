from sqlalchemy import MetaData
from sqlalchemy.orm import declared_attr, declarative_base

class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

metadata_obj = MetaData(schema='collect')
Base = declarative_base(cls=Base, metadata=metadata_obj)