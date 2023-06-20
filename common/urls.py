from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register(r'service', ServiceImageViewSet, basename='service')
# router.register(r'about-us', AboutAPIViewSet, basename='about-us')
# router.register(r'staff', StaffViewSet, basename='staff')
# router.register(r'project', ProjectViewSet, basename='project')
# router.register(r'statistic', StatisticViewSet, basename='statistic')

urlpatterns = [
    # path('', include(router.urls)),
    path('about-us/', AboutAPIView.as_view(), name='about-us'),
    path('service/', ServiceImageView.as_view(), name='service'),
    path('project/', ProjectAPIView.as_view(), name='project'),
    path('statistic/', StatisticAPIView.as_view(), name='statistic'),
    path('staff/', StaffAPIView.as_view(), name='staff'),
    path('sponsor/', SponsorAPIView.as_view(), name='sponsor'),
    path('portfolio/', PortfolioImageView.as_view(), name='portfolio'),
    path('service-create/', ServiceAPIView.as_view(), name='service-create'),
    path('email-post/', EmailPostView.as_view(), name='email-post'),
    # path('email-list/', EmailListView.as_view(), name='email-list'),
    # path('portfolio-create/', PortfolioAPIView.as_view(), name='portfolio-create')
]


