from django.db import models

# Create your models here.
class Trait(models.Model):
	trait_name = models.CharField(max_length=200)

class Population(models.Model):
	population_name = models.CharField(max_length=200)