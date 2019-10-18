from django.db import models

class Book(models.Model):
	title=models.CharField(max_length=100)
	author=models.CharField(max_length=100)
	pdf=models.FileField(upload_to='docs')
	cover=models.ImageField(upload_to='pics', null=True, blank=True)

	def __str__(self):
		return self.title