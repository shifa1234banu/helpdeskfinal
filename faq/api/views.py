from django.shortcuts import render
from faq.models import Faq
from rest_framework.response import Response
from faq.api.serializers import FaqSerializer
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


class FaqListAV(APIView):
    def get(self, request):
        faqs = Faq.objects.all()
        serializer = FaqSerializer(faqs, many=True)
        return Response(serializer.data) 

    def post(self, request):
        serializer = FaqSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        else:
            return Response(serializer.errors)


class FaqAV(APIView):

    def get(self, request, pk):
        try:
            faq = Faq.objects.get(pk=pk)
        except Faq.DoesNotExist:
            return Response({'Error':'organization not found'}, status=status.HTTP_404_NOT_FOUND)    

        serializer = FaqSerializer(faq)
        return Response(serializer.data)



    def put(self, request, pk):

        faq = Faq.objects.get(pk=pk)
        serializer = FaqSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):

        faq = Faq.objects.get(pk=pk)
        faq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)