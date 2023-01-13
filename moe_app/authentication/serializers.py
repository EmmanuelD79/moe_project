from rest_framework import serializers
from .models import Contact, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.shortcuts import get_object_or_404

class ContactSerializer(serializers.ModelSerializer):
    
    owner_email = serializers.EmailField(max_length=None, min_length=3, allow_blank=False, write_only=True)
    
    class Meta:
        model = Contact
        fields = ['id',
                  'email', 
                  'birthday',
                  'is_private', 
                  'first_name',
                  'last_name',
                  'title',
                  'company',
                  'sub_type',
                  'phone',
                  'mobile',
                  'address',
                  'zip_code',
                  'city',
                  'country',
                  'url',
                  'photo_original',
                  'owner',
                  'owner_email'
                  ]
        extra_kwargs = {
            'id': {'read_only': True},
            'owner': {'read_only': True},
            'owner_email': {'write_only': True}, 
        }
    
    def create(self, validated_data):
        owner_email = validated_data.pop('owner_email')
        user = User.objects.filter(email=owner_email)
        active_user = get_object_or_404(user)
        validated_data['owner'] = active_user
        return super().create(validated_data)
        

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
        )
    
    class Meta:
        model = User
        fields = ['email', 'password']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['is_guest'] = user.is_guest
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        # ...

        return token


class SignupSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
        )
    password2 = serializers.CharField(
        label='Confirmer le mot de passe',
        write_only=True,
        required=True,
        style={"input_type": "password"})

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name',
                  'last_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            password=validated_data['password']
        )

        return user
