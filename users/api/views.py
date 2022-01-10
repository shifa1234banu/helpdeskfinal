from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from rest_framework import generics

from rest_framework_simplejwt.tokens import RefreshToken

from users.api.serializers import UserRegistrationSerializer


# Create your views here.

@api_view(['POST',])

def user_registration_view(request):

    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'Registration successful'
            data['username'] = account.username
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access':str(refresh.access_token),

            }
            

        else:
            data = serializer.errors
        
        
        return Response(data)


@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)        
