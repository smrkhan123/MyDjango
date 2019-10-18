from django.db import models

# Create your models here.
class Article(models.Model):
	title=models.CharField(max_length=100)
	body=models.TextField(max_length=500)
	author=models.CharField(max_length=50)
	adate=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
