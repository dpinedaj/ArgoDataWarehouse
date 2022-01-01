import click
import sys
sys.path.insert(0,"/mnt/g/My Drive/local/projects/ArgoDataWarehouse/src")

from argodw.core.controllers import *
from argodw.adapters.data_modeler import DataModeler

INSTALLED_DATASETS = {
    "fire_incidents": [RawFireIncidentsController(), ProcessedFireIncidentsController()]
}

# TODO: click receive parameters to run
# TODO: El proceso debe traer los datos de la fuente, crear las particiones en raw y guardar todo como string
#       Luego debe procesar los campos (una breve limpieza por tipo de dato), crear particiones en processed y guardar
# TODO: Mirar la idea del setup.py build e install para usar como comando bash

@click.command()
@click.option('--dataset')
def cli(dataset):
    assert dataset in INSTALLED_DATASETS,\
    f"dataset {dataset} is not installed, available options: {list(INSTALLED_DATASETS.keys())}"

    controllers = INSTALLED_DATASETS[dataset]
    dm = DataModeler()
    dm.start(controllers)


cli()