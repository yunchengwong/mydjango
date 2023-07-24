from django.db import models
from django.core import validators

# Create your models here.

class Auto(models.Model):
    name = models.CharField(max_length=200, validators=[validators.MinValueValidator(2,"Make must be greater than 1 character")])
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.name
    
class Make(models.Model):
    name = models.CharField(max_length=200, validators=[validators.MinValueValidator(2,"Make must be greater than 1 character")], help_text="Enter a Auto manufacturer")
    
    def __str__(self):
        return self.name