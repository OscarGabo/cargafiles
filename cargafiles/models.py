from __future__ import unicode_literals

from django.db import models

# Create your models here.
class File(models.Model):
	nombre = models.CharField(max_length=255)
	fecha = models.DateField()

	def __str__ (self):
		return self.nombre