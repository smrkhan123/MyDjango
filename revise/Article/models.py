from django.db import models

class Article(models.Model):
	title=models.CharField(max_length=100)
	body=models.TextField(max_length=500)
	adate=models.DateTimeField(auto_now_add=True)
	author=models.CharField(max_length=100)
	
	def __str__(self):
		return self.title

	
