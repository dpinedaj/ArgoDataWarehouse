from typing import Dict
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.attributes import InstrumentedAttribute


raw_meta = MetaData(schema='raw')
Raw = declarative_base(metadata=raw_meta)

processed_meta = MetaData(schema='processed')
Processed = declarative_base(metadata=processed_meta)



class MapeableBase():
    @classmethod
    def get_json_schema(cls) -> Dict[str, str]:
        columns = {c:t for c, t in cls.__dict__.items() if isinstance(t, InstrumentedAttribute)}
        columns = {c:str(t.type) for c, t in columns.items()}
        return columns