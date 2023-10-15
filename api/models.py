from django.db import models

# Create your models here.
class DwellingType(models.Model):
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_name

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dwelling(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    dwelling_type = models.ForeignKey(DwellingType, on_delete=models.CASCADE, null=True, default=None)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    photos = models.ManyToManyField('Photo')
    guests = models.IntegerField()
    area = models.FloatField()
    features = models.JSONField(default=list)
    bedroom = models.JSONField(default=list)
    kitchen = models.JSONField(default=list)
    bathroom = models.JSONField(default=list)
    occupied_dates = models.ManyToManyField('OccupiedDate')

    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f'Photo {self.id}'
    
class OccupiedDate(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"from {self.check_in} to {self.check_out}" 
