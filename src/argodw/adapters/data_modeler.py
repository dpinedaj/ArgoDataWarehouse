from typing import List
import time

from argodw.ports import Process
from argodw.core.controllers import *

class DataModeler(Process):
    def __init__(self):
        self.max_retries = 3
        self.retries = 0
        self.wait_time = 30

    def run_controller(self, controller: DataController) -> None:
        controller.retrieve()
        controller.process()
        controller.save()

    def start(self, controllers: List[DataController]) -> None:
        for controller in controllers:
            try:
                self.run_controller(controller)
            except Exception as e:
                print(str(e))
                self.retry(controller)
                

    def retry(self, controller: DataController) -> None:
        while self.retries < self.max_retries:
            try:
                time.sleep(self.wait_time)
                self.run_controller(controller)
                return
            except:
                self.retries += 1
                print(f"Retry {self.retries} failed...")
        else:
            print("Max Retries reached, skipping...")
            self.retries = 0
