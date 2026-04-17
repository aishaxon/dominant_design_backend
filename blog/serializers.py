from rest_framework import serializers
from .models import *


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class VideoProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoProject
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class PricingSerializer(serializers.ModelSerializer):
    features_list = serializers.SerializerMethodField()

    class Meta:
        model = Pricing
        fields = '__all__'

    def get_features_list(self, obj):
        return obj.features.split('\n')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'