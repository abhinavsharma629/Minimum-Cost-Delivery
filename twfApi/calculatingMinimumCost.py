import re,math
def calculatingMinimumCost(orderDictionary, centerProductWeightDictionary):
	# Traversing the order and calculating total orders of each center
	centerC1TotalOrder=0
	centerC2TotalOrder=0
	centerC3TotalOrder=0

	for i,j in orderDictionary.items():
		if(re.match(r'[A-C]', i)):
			centerC1TotalOrder+=(int)(centerProductWeightDictionary['C1'][i])*(float)(j)
		elif(re.match(r'[D-F]', i)):
			centerC2TotalOrder+=(int)(centerProductWeightDictionary['C2'][i])*(float)(j)
		else:
			centerC3TotalOrder+=(int)(centerProductWeightDictionary['C3'][i])*(float)(j)

	
	totalOrderQuantity=centerC1TotalOrder+centerC2TotalOrder+centerC3TotalOrder
	
	noOfVisits=math.floor(totalOrderQuantity/100)
	noOfExtraQuantity=(totalOrderQuantity/100)-noOfVisits
	totalMinimumCost=noOfVisits*(10+(95/5)*8)
	extraVisitCost=(noOfExtraQuantity*100)
	totalMinimumCost+=10+((math.ceil((extraVisitCost-5)/5))*8)
	
	return [totalMinimumCost, centerC1TotalOrder, centerC2TotalOrder, centerC3TotalOrder]