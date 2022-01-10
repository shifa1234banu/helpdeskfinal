from rest_framework import serializers
from organization.models import Category,Organization


class CategorySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Category
        fields = ['name',]
        
class OrganizationSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer
    class Meta:
        model = Organization
        fields = ['name','category']

    


    
    


