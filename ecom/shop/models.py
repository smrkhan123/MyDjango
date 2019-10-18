from django.db import models

# Create your models here.
class Product(models.Model):
	product_id = models.AutoField
	product_name = models.CharField(max_length=100)
	desc = models.CharField(max_length=1000)
	category = models.CharField(max_length=100,default="")
	subcategory = models.CharField(max_length=100,default="")
	price = models.IntegerField(default=0)
	Image = models.ImageField(upload_to="shop/images",default="")
	pub_date = models.DateField()

	def __str__(self):
		return self.product_name

class Contact(models.Model):
	msg_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100,default="")
	email = models.CharField(max_length=100,default="")
	desc = models.CharField(max_length=1000,default="")
	phonr = models.CharField(max_length=70,default="")

	def __str__(self):
		return self.name
