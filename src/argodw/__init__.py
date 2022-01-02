from argodw.adapters.data_modeler import DataModeler
from argodw.core.controllers import *
import click



INSTALLED_DATASETS = {
    "fire_incidents": [RawFireIncidentsController(), ProcessedFireIncidentsController()]
}


@click.command()
@click.option('--dataset')
def cli(dataset):
    assert dataset in INSTALLED_DATASETS,\
        f"dataset {dataset} is not installed, available options: {list(INSTALLED_DATASETS.keys())}"

    controllers = INSTALLED_DATASETS[dataset]
    dm = DataModeler()
    dm.start(controllers)