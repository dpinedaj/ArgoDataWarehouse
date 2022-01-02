import requests
import pandas as pd
from io import BytesIO
from datetime import date, timedelta
from tqdm import tqdm

from argodw.ports import DataController
from argodw.core.models import RawFireIncidentsModel, ProcessedFireIncidentsModel
from argodw.core.utils.db_utils import get_session
from argodw.core.utils.commons import fix_data_schema, clear_columns_names


current_date = date.today().strftime("%Y-%m-%d")
tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")


class RawFireIncidentsController(DataController):
    data_source = 'https://data.sfgov.org/api/views/wr8u-xric/rows.csv?accessType=DOWNLOAD'

    def retrieve(self):
        schema = RawFireIncidentsModel.get_json_schema(pandas=True)
        retrieve_data = requests.get(self.data_source)
        content = BytesIO(retrieve_data.content)
        self.data = pd.read_csv(content, sep=",", dtype=schema)

    def process(self):
        self.data = self.data.astype(str)
        self.data = clear_columns_names(self.data)
        self.data_dict = self.data.to_dict('records')

        with get_session() as (session, _):
            session.execute(f"""
            CREATE TABLE {RawFireIncidentsModel.name()}_{current_date.replace('-', '_')}
            PARTITION OF {RawFireIncidentsModel.name()}
            FOR VALUES FROM ('{current_date}') to ('{tomorrow}')
            """)
            session.commit()

    def save(self):
        with get_session() as (session, _):
            for d in tqdm(self.data_dict):
                d.update({"CurrentDate": current_date})
                t = RawFireIncidentsModel(**d)
                session.add(t)

            session.commit()

    def __repr__(self):
        return "RawFireIncidents"


class ProcessedFireIncidentsController(DataController):
    def retrieve(self):
        source_table_name = RawFireIncidentsModel.name()
        with get_session() as (_, engine):
            self.data = pd.read_sql(
                f"SELECT * FROM {source_table_name} where \"CurrentDate\"='{current_date}'",
                engine)

    def process(self):
        schema = ProcessedFireIncidentsModel.get_json_schema()
        self.data = fix_data_schema(self.data, schema)
        self.data = clear_columns_names(self.data)
        self.data_dict = self.data.to_dict('records')

        with get_session() as (session, _):
            session.execute(f"""
            CREATE TABLE {ProcessedFireIncidentsModel.name()}_{current_date.replace('-', '_')}
            PARTITION OF {ProcessedFireIncidentsModel.name()}
            FOR VALUES FROM ('{current_date}') to ('{tomorrow}')
            """)
            session.commit()

    def save(self):
        with get_session() as (session, _):
            for d in tqdm(self.data_dict):
                d.update({"CurrentDate": current_date})
                t = ProcessedFireIncidentsModel(**d)
                session.add(t)

            session.commit()

    def __repr__(self):
        return "ProcessedFireIncidents"
