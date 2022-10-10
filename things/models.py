from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator

# Create your models here.

class Thing(models.Model):
    name = models.CharField(
        max_length = 30,
        unique = True
    )
    description = models.TextField(
        blank = True,
        validators=[MaxLengthValidator(120)]
    )
    quantity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)]
    )
