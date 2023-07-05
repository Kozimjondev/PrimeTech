from modeltranslation.translator import translator, TranslationOptions, register
from .models import Service, AboutUs, Statistic, Portfolio


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Statistic)
class StatisticTranslationOptions(TranslationOptions):
    fields = ('statistic_name', )


@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

