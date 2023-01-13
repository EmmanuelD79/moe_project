from rest_framework import serializers
from .models import Company, CompanyCategory
from authentication.models import User
from django.shortcuts import get_object_or_404


class CompanyCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyCategory
        fields = ['id', 'name']


class CompanySerializer(serializers.ModelSerializer):

    category = CompanyCategorySerializer()

    owner_email = serializers.EmailField(
        max_length=None, min_length=3, allow_blank=False, write_only=True)

    class Meta:
        model = Company
        fields = ['id',
                  'legal_name',
                  'identification_code',
                  'identification_type',
                  'company_group',
                  'category',
                  'status',
                  'phone',
                  'mobile',
                  'address',
                  'zip_code',
                  'city',
                  'country',
                  'website',
                  'owner',
                  'owner_email'
                  ]

        extra_kwargs = {
            'id': {'read_only': True},
            'owner_email': {'write_only': True},
        }

    def create(self, validated_data):
        owner_email = validated_data.pop('owner_email')
        user = User.objects.filter(email=owner_email)
        active_user = get_object_or_404(user)
        validated_data['owner'] = active_user
        return super().create(validated_data)
