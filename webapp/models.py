from django.db import models

class Users(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    Data = models.TextField()

    def __str__(self):
        return self.Data

class csvDb(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    DataBase = models.TextField()

    def __str__(self):
        return self.DataBase
