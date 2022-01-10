from django.shortcuts import render
from organization.models import Organization,Category
from rest_framework.response import Response
from organization.api.serializers import CategorySerializer,OrganizationSerializer
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class CategoryListAV(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data) 

    def post(self, request):
        serializer = CategorySerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        else:
            return Response(serializer.errors)


class CategoryAV(APIView):

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'Error':'organization not found'}, status=status.HTTP_404_NOT_FOUND)    

        serializer = CategorySerializer(category)
        return Response(serializer.data)



    def put(self, request, pk):

        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):

        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)            


class OrganizationListAV(APIView):
    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data) 

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        else:
            return Response(serializer.errors)


class OrganizationAV(APIView):

    def get(self, request, pk):
        try:
            organization = Organization.objects.get(pk=pk)
        except Organization.DoesNotExist:
            return Response({'Error':'organization not found'}, status=status.HTTP_404_NOT_FOUND)    

        serializer = OrganizationSerializer(organization)
        return Response(serializer.data)



    def put(self, request, pk):

        organization = Organization.objects.get(pk=pk)
        serializer = OrganizationSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):

        organization = Organization.objects.get(pk=pk)
        organization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)