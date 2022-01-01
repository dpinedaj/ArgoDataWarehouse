from typing import Dict
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.attributes import InstrumentedAttribute


PANDAS_EQUIVALENCE = {"NUMERIC": float, "VARCHAR": str}

class MapeableBase():
    @classmethod
    def get_json_schema(cls, pandas=False) -> Dict[str, str]:
        columns = {t.name: str(t.type) for t in cls.__dict__.values(
        ) if isinstance(t, InstrumentedAttribute)}
        if pandas:
            columns = {c: PANDAS_EQUIVALENCE.get(t, str) for c, t in columns.items()}
        
        return columns

    @classmethod
    def name(cls):
        return cls.metadata.schema + '.' + cls.__tablename__



raw_meta = MetaData(schema='raw')
Raw = declarative_base(cls=MapeableBase, metadata=raw_meta)

processed_meta = MetaData(schema='processed')
Processed = declarative_base(cls=MapeableBase, metadata=processed_meta)

