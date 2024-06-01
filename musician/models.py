from django.db import models

# Create your models here.

class MusicianModel(models.Model):
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    Email=models.EmailField()
    Phone=models.CharField(max_length=12)
    Instrument_Type=models.CharField(max_length=30)


    def __str__(self):
        return self.First_name
    