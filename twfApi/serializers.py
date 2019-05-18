from rest_framework import serializers
from .models import centerData, productWeightData

class centerDataSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=centerData  # what module you are going to serialize
		fields= '__all__'

class productWeightDataSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=productWeightData  # what module you are going to serialize
		fields= '__all__'