from django.db import models
from django.db.models.fields import TextField

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    review = TextField()

    def __str__(self):
        return f"{self.title} ({self.year})"

# Create your models here.
