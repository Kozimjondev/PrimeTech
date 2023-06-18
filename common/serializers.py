from rest_framework import serializers
from .models import *


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'description')


class ServiceImageSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = ServiceImage
        fields = ('service', 'image')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('name', 'description')


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('full_name', 'profession', 'avatar')


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ('client', 'support', 'project', 'freelance')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectNumber
        fields = ('web_site', 'mobile_app', 'crm', 'telegram_bot')


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ("email", 'phone_number', 'message')


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'image')


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('name', 'description')


class PortfolioImageSerializer(serializers.ModelSerializer):
    portfolio = PortfolioSerializer(read_only=True)

    class Meta:
        model = PortfolioImage
        fields = ('portfolio', 'image')