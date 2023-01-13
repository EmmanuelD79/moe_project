from django.shortcuts import render
from rest_framework import viewsets, status, response
from .serializers import CompanySerializer, CompanyCategorySerializer
from .models import Company, CompanyCategory

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCategorySerializer
    queryset = CompanyCategory.objects.all()
    
    def create(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
