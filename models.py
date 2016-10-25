from django.db import models
from pipeline.models import AviJob


class TutorialModel(AviJob):
    # fib_num = models.IntegerField()
    pipeline_task = "CalcFib"
