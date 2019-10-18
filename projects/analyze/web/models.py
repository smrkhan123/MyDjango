from django.db import models
Default='media/img/destination_3.jpg'
# Create your models here.
class Destination(models.Model):

	name = models.CharField(max_length=100)
	img = models.ImageField(upload_to='img',default=Default)
	desc = models.TextField()
	price = models.IntegerField()
	offer = models.BooleanField(default=False)