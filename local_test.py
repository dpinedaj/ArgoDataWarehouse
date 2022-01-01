from sqlalchemy import MetaData, Column, Integer, VARCHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.attributes import InstrumentedAttribute



metadata_obj = MetaData(schema='raw')
Base = declarative_base(metadata=metadata_obj)
class MapeableBase():
    @classmethod
    def get_json_schema(cls):
        columns = {c:t for c, t in cls.__dict__.items() if isinstance(t, InstrumentedAttribute)}
        columns = {c:str(t.type) for c, t in columns.items()}
        return columns

class Test(Base, MapeableBase):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True, nullable=False)
    test = Column(VARCHAR, nullable=True)



cols = Test.get_json_schema()
