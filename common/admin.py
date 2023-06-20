from django.contrib import admin
from .models import *

# admin.site.register(Service)
# admin.site.register(ServiceImage)
admin.site.register(AboutUs)
admin.site.register(Statistic)
admin.site.register(Staff)
admin.site.register(ProjectNumber)
# admin.site.register(Portfolio)
# admin.site.register(PortfolioImage)
admin.site.register(Sponsor)
admin.site.register(Email)


class ImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 2


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 2


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageInline]