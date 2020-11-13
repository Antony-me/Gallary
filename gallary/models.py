from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length =60)
 
    
class Cartegory(models.Model):
    name=models.CharField(max_length =30) 

    def __str__(self):
        return self.name
   

class Photo(models.Model):
    image = models.ImageField(max_length =30)
    image_name = models.CharField(max_length =60)
    image_description = models.CharField(max_length =120)
    location = models.ForeignKey(Location,  on_delete = models.CASCADE)
    cartegory = models.ForeignKey(Cartegory,  on_delete = models.CASCADE)

