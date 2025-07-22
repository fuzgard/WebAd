from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address