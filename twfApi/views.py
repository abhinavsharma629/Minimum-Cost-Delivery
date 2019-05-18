from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import re
from .centerProductWeightDictionary import centerProductWeightDictionary
from .calculatingMinimumCost import calculatingMinimumCost
'''from .models import centerData, productWeightData
from .serializers import centerDataSerializer, productWeightDataSerializer
from django.core import serializers'''

@api_view(['GET'])
def getMinimumCost(request):
	#Get Data
	data=request.GET

	#Initializing order dictionary
	orderDictionary={}

	#Filling the Order dictionary if products are in stock else return error
	try:
		for i in data:
			if(re.match(r'[A-Ia-i]', i)):
				orderDictionary[i]=data[i]
			else:
				return Response({"Error Message": "Product/s Out Of List/Stock"}, status=status.HTTP_204_NO_CONTENT)
	except:
		return Response({"Error Message": "Product/s Out Of List/Stock"}, status=status.HTTP_204_NO_CONTENT)
	
	'''If no error encountered then calculation for the minimum cost
	taking in consideration that one vehicle can carry 100 kg at max at one time
	and the cost of running vehicle is 0-5 kg Rs. 10 and for every additional 5kg Rs 8
	Distance of centers as given from L(customer) :- 
	C1->L = 3 units
	C2->L = 2.5 units
	C3->L = 2 units
	C1->C2 = 4 units
	C2->C3 = 3 units'''

	dataOfOrder=calculatingMinimumCost(orderDictionary, centerProductWeightDictionary)
	
	'''Way Of traversing Json Field in Postgres in case of retrieving data from db:- 
	print(productWeightData.objects.filter(centerdata__C1__A="3"))
	data = serializers.serialize("json", productWeightData.objects.all(), fields=('centerdata'))'''
	
	return Response({
		'MinimumCostRequired': "Rs. "+str("{0:.2f}".format(dataOfOrder[0])),
		'Total Quantity Ordered From Center C1': str("{0:.2f}".format(dataOfOrder[1]))+" units",
		'Total Quantity Ordered From Center C2': str("{0:.2f}".format(dataOfOrder[2]))+" units",
		'Total Quantity Ordered From Center C3': str("{0:.2f}".format(dataOfOrder[3]))+" units"
		}, status=status.HTTP_200_OK)