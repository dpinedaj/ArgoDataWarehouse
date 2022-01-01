import requests
import pandas as pd
from io import BytesIO

from argodw.core.controllers.data_controller import DataController
from argodw.core.models import RawFireIncidentsModel, ProcessedFireIncidentsModel
from argodw.core.utils.db_utils import get_session
from argodw.core.utils.commons import fix_data_schema

class RawFireIncidentsController(DataController):
    data_source = 'https://data.sfgov.org/api/views/wr8u-xric/rows.csv?accessType=DOWNLOAD'

    def retrieve(self):
        retrieve_data = requests.get(self.data_source)
        content = BytesIO(retrieve_data.content)
        self.data = pd.read_csv(content, sep=",")
        self.columns = self.data.columns

    def process(self):
        self.data = self.data.astype(str)
        self.data_dict = self.data.to_dict('record')

    def save(self):
        with get_session() as session:
            for d in self.data_dict:
                t = RawFireIncidentsModel(**d)
                session.add(t)

            session.commit()

class ProcessedFireIncidentsController(DataController):
    def retrieve(self):
        pass

    def process(self):
        schema = ProcessedFireIncidentsModel.get_json_schema()
        self.data = fix_data_schema(self.data, schema)

    def save(self):
        pass