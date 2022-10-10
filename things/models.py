from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(
        max_length = 30,
        unique = True
    )
    description = models.TextField(
        blank = True,
        max_length = 120
    )
    quantity = models.IntegerField(
        min_value = 0,
        max_value = 100
    )
