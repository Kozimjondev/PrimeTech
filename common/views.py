from rest_framework import status, mixins
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .custompermissions import IsAdminUserOrReadOnly
from .models import Service, AboutUs, Staff, ProjectNumber, Statistic
from rest_framework.permissions import AllowAny, IsAdminUser
from datetime import datetime, timedelta
from rest_framework.exceptions import ValidationError


class ServiceAPIView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary="Xizmatlar ro'yhati")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Xizmatlar yaratish")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ServiceImageViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          GenericViewSet):
    queryset = ServiceImage.objects.all()
    serializer_class = ServiceImageSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary='Xizmatlarni rasmlar bilan birga yaratish')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Har bir Xizmatni ko`rish')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Har bir Xizmatni o`zgartirish")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Har bir Xizmatni delete qilish')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AboutAPIViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary='Biz haqimizdani yaratish')
    def create(self, request, *args, **kwargs):
        # Check if an object already exists
        if AboutUs.objects.exists():
            return Response("Only one object can be created.", status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Biz haqimizda malumotni olish')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Biz haqimizda malumotni ozgartirish")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Biz haqimizda malumotni o`chirish')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class StaffViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary="Xodimlar ro`yhati")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Xodim yaratish')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Har bir xodimni ko`rish')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Har bir xodimni o`zgartirish")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Har bir xodimni ochirish')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ProjectViewSet(ModelViewSet):
    queryset = ProjectNumber.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary='Mijozlar sonlarini yaratish. '
                                           'Faqat 1 marta yaratish mumkin -- about page dagi')
    def create(self, request, *args, **kwargs):
        # Check if an object already exists
        if ProjectNumber.objects.exists():
            return Response("Only one object can be created.", status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Mijozlar statistikani olish")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Yaratilgan Mijozlar statistikani ko`rish')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Yaratilgan Mijozlar statistikani o'zgartirish")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Yaratilgan Mijozlar statistikani o`chirish')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class StatisticViewSet(ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary='Proyekt sonlarini yaratish. '
                                           'Faqat 1 marta yaratish mumkin -- about page dagi')
    def create(self, request, *args, **kwargs):
        # Check if an object already exists
        if Statistic.objects.exists():
            return Response("Only one object can be created.", status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Proyekt statistikani olish")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Yaratilgan Proyekt statistikani ko`rish')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Yaratilgan Proyekt statistikani o'zgartirish")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Yaratilgan Proyekt statistikani o`chirish')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class EmailPostView(CreateAPIView):
    serializer_class = EmailSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(operation_summary='Email telefon raqam va xabar qoldirish')
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')

        # Get the current date
        today = datetime.now().date()

        # Count the number of times the email or phone number has been posted today
        email_post_count = Email.objects.filter(email=email, created_at__date=today).count()
        phone_post_count = Email.objects.filter(phone_number=phone_number, created_at__date=today).count()

        # Check if the limit has been reached
        if email_post_count >= 5 or phone_post_count >= 5:
            raise ValidationError("You have reached the maximum limit of posts for email or phone number.")

        return super().create(request, *args, **kwargs)


class EmailListView(ListAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(operation_summary='Jonatilgan email xabarlar ro`yhatini olish')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SponsorAPIView(ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary="Xamkorlarimiz ro'yhati")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Xamkor yaratish")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Har bir xamkorni ko'rish")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Har bir xamkorni oz'gartirish")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Har bir xamkorni o'chirish")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class PortfolioAPIView(CreateAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(operation_summary="Portfolio yaratish faqat admin uchun")
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PortfolioImageView(ModelViewSet):
    queryset = PortfolioImage.objects.all()
    serializer_class = PortfolioImageSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    @swagger_auto_schema(operation_summary="Portfolio ro'yhati")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Portfolio rasm bilan birga yaratish')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Portfolioni ko'rish")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Portfolioni o'zgartirish")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Portfolioni o'chirish")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)