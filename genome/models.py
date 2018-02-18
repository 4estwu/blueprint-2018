from django.db import models
import genomelink

# Create your models here.
class Trait(models.Model):
	trait_name = models.CharField(max_length=200)
	#report = genomelink.Report.fetch(name=self, population='european', token='GENOMELINKTEST001').summary['text']

	@property
	def blah(self):
		return 'blah'

	@property
	def report(self):
		return genomelink.Report.fetch(name=self, population='european', token='GENOMELINKTEST001').summary['text']

class Person(models.Model):
	person_genome = models.CharField(max_length=200)