from django.db import models

class Treasury(models.Model):
	year1 = models.TextField(max_length=10000)
	year2 = models.TextField(max_length=10000)
	year3 = models.TextField(max_length=10000)

	def __str__(self):
		return self.year1