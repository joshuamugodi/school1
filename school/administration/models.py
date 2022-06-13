from django.db import models

# Create your models here.

class school_recordsJ(models.Model):
	"""docstring for school_records"""
	firstname = models.CharField(max_length=40)
	lastname = models.CharField(max_length=40)
	Class = models.CharField(max_length=3)
	Examnumber= models.CharField(max_length=12,primary_key=True)
	g7 = models.CharField(max_length=3)
	def __str__(self):
		return self.firstname


class school_recordsS(models.Model):
	"""docstring for school_records"""
	firstname = models.CharField(max_length=40)
	lastname = models.CharField(max_length=40)
	Class = models.CharField(max_length=3)
	Examnumber= models.CharField(max_length=12, primary_key=True)
	g9 = models.CharField(max_length=3)
	def __str__(self):
		return self.firstname