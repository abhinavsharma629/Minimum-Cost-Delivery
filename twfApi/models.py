from django.db import models
from django.contrib.postgres.fields import JSONField
from .productChoice import PRODUCT_CHOICE
from .centerChoice import CENTER_CHOICE

#Efficient Way To Store Data
#Product - Weight Data
class productWeightData(models.Model):
    centerdata = JSONField()


# Another Way To Store Data
#Center - Product Data
class centerData(models.Model):
	name=models.CharField(choices=CENTER_CHOICE, max_length=100, null=False)
	productName=models.CharField(choices=PRODUCT_CHOICE, max_length=100, null=False)
	
	def __str__(self):
		return self.name