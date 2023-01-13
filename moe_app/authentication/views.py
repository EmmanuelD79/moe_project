from django.shortcuts import render
from .models import Contact, User
from .serializers import ContactSerializer, LoginSerializer, MyTokenObtainPairSerializer, SignupSerializer
from rest_framework import viewsets, status, response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    

    def create(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return response.Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            refresh = MyTokenObtainPairSerializer.get_token(user)
            return response.Response({'msg': 'Login Success', 'token': {'refresh': str(refresh), 'access': str(refresh.access_token)}}, status=status.HTTP_200_OK)
        return response.Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class SignupView(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({
            'msg': 'User is created',
            'user': serializer.data,
        })
