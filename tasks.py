"""
GAVIP Example AVIS: Simple AVI

An example AVI pipeline is defined here, consisting of three tasks:

- DummyTask - demonstrates dependencies, but does nothing
- DownloadData - uses services.gacs.GacsQuery to run ADQL queries in GACS(-dev)
- ProcessData - generates a simple scatter plot with Bokeh from the downloaded data
@req: REQ-0006
@comp: AVI Web System
"""
import os
from django.conf import settings
# Class used for creating pipeline tasks
from pipeline.classes import (
    AviTask,
    AviLocalTarget,
)
import numpy as np


def list_1():
    a=np.array([ 100, 4, 100, 7, 10, 17, 0, 100, 2, -4, 17, 4, 11, 100])
    return a


class CalcFib(AviTask):
    # fib_num = AviParameter()

    def output(self):
        return AviLocalTarget(os.path.join(
            settings.OUTPUT_PATH,
            "list_1.txt"
        ))

    def run(self):
        list_result = list_1()
        with open(self.output().path, 'wb') as out:
            print(list_result)
            list_result = bytes(str(list_result), encoding="UTF-8")
            out.write(list_result)
