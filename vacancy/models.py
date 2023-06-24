from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
from .region import DISTRICTS
from django.core.validators import MaxValueValidator


class Technology(models.Model):
    name = models.CharField(_("technology"), max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    WORK_TYPE = (
        ('internship', 'amaliyot'),
        ('work', 'ish'),
    )

    company = models.CharField(_("company"), max_length=150, blank=True, null=True)
    age = ArrayField(models.PositiveIntegerField(), verbose_name=_("ages [from, to]"))
    technologies = models.ManyToManyField(Technology, verbose_name=_("technologies"))
    work_time = models.CharField(_("work time"), max_length=50, blank=True, null=True)
    additional_info = models.CharField(_("additional information"), max_length=1000, blank=True, null=True)
    work_type = models.CharField(_("work type"), choices=WORK_TYPE, default=WORK_TYPE[0][0], max_length=15)
    salary = models.CharField(_("salary"), max_length=50, blank=True, null=True)
    districts = models.CharField(_("salary"), max_length=50, choices=DISTRICTS, default=DISTRICTS[9][0])
    is_student = models.BooleanField(_("is student"), default=False)
    username = models.CharField(_("username"), max_length=50, blank=True, null=True)
    apply_time = models.CharField(_("apply time"), max_length=50, blank=True, null=True)
    is_available = models.BooleanField(_("is available"), default=True)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'vacancy'
        verbose_name_plural = 'vacancies'


class VacancyJob(models.Model):
    full_name = models.CharField(_("Full name"), max_length=100)
    technology = models.ManyToManyField(Technology, verbose_name=_("Technology"))
    purpose = models.CharField(_("Purpose"), max_length=1000)
    region = models.CharField(_("Region"), max_length=100)
    contact = models.CharField(_("Contact"), max_length=200,
                               help_text='Telefon raqam va telegram linkni qoldiring.')
    portfolio = models.FileField(_("Portfolio link"), blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Vacancy job")
        verbose_name_plural = _("Vacancy jobs")



