from django.db import models

# Create your models here.

class Lender(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	email = models.EmailField(max_length = 254)



class Slot(models.Model):
	date = models.DateField(null=True, blank=True)
	time = models.TimeField(null=True, blank=True)
	idd = models.CharField(max_length=19,null=True)
	count = models.IntegerField(default=3)
	c1 = models.IntegerField(default=0)
	c2 = models.IntegerField(default=0)
	c3 = models.IntegerField(default=0)



class Borrower(models.Model):
	roll_no = models.CharField(max_length=21)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=1000)
	mobile = models.CharField(max_length=10)
	date = models.DateField(null=True, blank=True)
	time = models.TimeField(null=True, blank=True)
	slot = models.ForeignKey(Slot,on_delete=models.CASCADE,default=1007)
	stationary = models.TextField(max_length=10000,blank=True,null=True)
	musical = models.TextField(max_length=10000,blank=True,null=True)
	book = models.TextField(max_length=10000,blank=True,null=True)
	check = models.BooleanField(default=False)












