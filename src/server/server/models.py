from django.db import models

from .config import ITEM_FIELDS

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    rate = models.IntegerField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {field: getattr(self, field) for field in ITEM_FIELDS}
