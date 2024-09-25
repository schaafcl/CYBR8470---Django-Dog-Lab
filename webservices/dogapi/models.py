from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Dog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Breed(models.Model):
    min_friendliness = 1
    max_friendliness = 5
    min_trainability = 1
    max_trainability = 5
    min_shedding = 1
    max_shedding = 5
    min_exercise = 1
    max_exercise = 5
    # referenced from https://docs.djangoproject.com/en/4.1/ref/models/fields/#enumeration-types
    class Sizes(models.TextChoices):
        # variable name  =  actual_name  ,  displayed_name
        TINY = 'T', 'Tiny'
        SMALL = 'S', 'Small'
        MEDIUM = 'M', 'Medium'
        LARGE = 'L', 'Large'
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=1, choices=Sizes.choices)
    friendliness = models.IntegerField(validators=[MinValueValidator(min_friendliness), MaxValueValidator(max_friendliness)])
    trainability = models.IntegerField(validators=[MinValueValidator(min_trainability), MaxValueValidator(max_trainability)])
    sheddingamount = models.IntegerField(validators=[MinValueValidator(min_shedding), MaxValueValidator(max_shedding)])
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(min_exercise), MaxValueValidator(max_exercise)])

    def __str__(self):
        return self.name

