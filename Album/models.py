from django.db import models
from musician.models import MusicianModel

Ratin_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]
# Create your models here.
class AlbumModel(models.Model):
    Album_name= models.CharField(max_length=20)
    musician= models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    Album_relese_date= models.DateField()
    Rating=models.CharField(max_length=50,choices=Ratin_CHOICES, default=1)

    def __str__(self):
        return self.Album_name
    
    