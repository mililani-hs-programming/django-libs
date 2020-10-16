from django.db import models

# Create your models here.
class Data(models.Model):
    Input = models.CharField(max_length=500)
    Ouput = models.CharField(max_length=500)

    def __str__(self):
        return self.Input
