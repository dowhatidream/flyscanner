from django.db import models


class Country(models.Model):
    cID = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
