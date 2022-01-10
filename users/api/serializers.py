from django.contrib.auth.models import User
from rest_framework import serializers




class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2 :
            raise serializers.ValidationError({'error':'Password should be the same'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email id already exists'})
        
        account = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            )
        account.set_password(password)
        account.save()

        return account