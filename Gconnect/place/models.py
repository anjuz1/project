from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=30, default='')
    login_id = models.BigIntegerField()

    def __str__(self):
        return self.name
