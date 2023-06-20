from rest_framework import status, mixins
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from .serializers import *
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .custompermissions import IsAdminUserOrReadOnly
from .models import Service, AboutUs, Staff, ProjectNumber, Statistic
from rest_framework.permissions import AllowAny, IsAdminUser
from datetime import datetime, timedelta
from rest_framework.exceptions import ValidationError


class ServiceAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary="Xizmatlar ro'yhati")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ServiceImageView(APIView):
    # queryset = ServiceImage.objects.all()
    # serializer_class = ServiceImageSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary='Har bir Xizmatni ko`rish')
    def get(self, request):
        queryset = ServiceImage.objects.all()
        serializer = ServiceImageSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


class AboutAPIView(APIView):
    # queryset = AboutUs.objects.all().last()
    # serializer_class = AboutSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary='Biz haqimizda malumot olish')
    def get(self, request):
        queryset = AboutUs.objects.all().last()
        serializer = AboutSerializer(queryset, many=False)
        return Response(serializer.data, status=200)


class StaffAPIView(ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary="Xodimlar ro`yhati")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProjectAPIView(APIView):
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary='Mijozlarga qilingan proyektlarni sonini ko`rish')
    def get(self, request):
        queryset = ProjectNumber.objects.all().last()
        serializer = ProjectSerializer(queryset, many=False)
        return Response(serializer.data, status=200)


class StatisticAPIView(APIView):
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary='Mijozlar, xamkorlar, loyihalar sonini korish')
    def get(self, request):
        queryset = Statistic.objects.all().last()
        serializer = StatisticSerializer(queryset, many=False)
        return Response(serializer.data, status=200)


class EmailPostView(CreateAPIView):
    serializer_class = EmailSerializer
    permission_classes = (AllowAny,)
    # throttle_classes = [AnonRateThrottle]
    http_method_names = ("post",)
    throttle_scope = "email-post"

    @swagger_auto_schema(operation_summary='Email telefon raqam va xabar qoldirish')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # @swagger_auto_schema(operation_summary='Email telefon raqam va xabar qoldirish')
    # def post(self, request, *args, **kwargs):
    #     email = request.data.get('email')
    #     phone_number = request.data.get('phone_number')
    #
    #     # Get the current date
    #     today = datetime.now().date()
    #
    #     # Count the number of times the email or phone number has been posted today
    #     email_post_count = Email.objects.filter(email=email, created_at__date=today).count()
    #     phone_post_count = Email.objects.filter(phone_number=phone_number, created_at__date=today).count()
    #
    #     # Check if the limit has been reached
    #     if email_post_count >= 5 or phone_post_count >= 5:
    #         raise ValidationError("You have reached the maximum limit of posts for email or phone number.")
    #
    #     return super().create(request, *args, **kwargs)


# class EmailListView(ListAPIView):
#     queryset = Email.objects.all()
#     serializer_class = EmailSerializer
#     permission_classes = (IsAdminUser,)
#
#     @swagger_auto_schema(operation_summary='Jonatilgan email xabarlar ro`yhatini olish')
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


class SponsorAPIView(APIView):
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary="Xamkorlarimiz ro'yhati")
    def get(self, request):
        queryset = Sponsor.objects.all()
        serializer = SponsorSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


# class PortfolioAPIView(CreateAPIView):
#     serializer_class = PortfolioSerializer
#     permission_classes = (IsAdminUser,)
#
#     @swagger_auto_schema(operation_summary="Portfolio yaratish faqat admin uchun")
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)


class PortfolioImageView(APIView):
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary="Portfolioni ko'rish")
    def get(self, request):
        queryset = PortfolioImage.objects.all().last()
        serializer = PortfolioImageSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
