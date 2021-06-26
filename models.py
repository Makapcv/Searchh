from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    rating = models.IntegerField()
