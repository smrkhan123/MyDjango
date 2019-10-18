from django.db import models

# Create your models here.
class Questions(models.Model):
	questions=models.CharField(max_length=200,unique=True)
	choice1=models.CharField(max_length=100,unique=False)
	choice2=models.CharField(max_length=100,unique=False)
	choice3=models.CharField(max_length=100,unique=False)
	choice4=models.CharField(max_length=100,unique=False)
	correct_answer=models.CharField(max_length=100,unique=False)