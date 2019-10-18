from django.db import models

class Destination(models.Model):
	name = models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics',default='',null=True,blank=True)
	file = models.FileField(upload_to='pics',null=True,blank=True)
	desc = models.TextField()
	price = models.IntegerField()
	offer = models.BooleanField(default=False)