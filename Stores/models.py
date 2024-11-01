from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100, unique=True)
    number = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} (#{self.number})"
