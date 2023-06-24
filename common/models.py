from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator, RegexValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))

    class Meta:
        abstract = True


class Service(BaseModel):
    name = models.CharField(_("Name"), max_length=200)
    description = models.TextField(_("Description"))

    # image = models.ImageField(_("Image"), upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")


class ServiceImage(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name=_("Service"),
                                related_name='images')
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.service.name

    class Meta:
        verbose_name = _("Service image")
        verbose_name_plural = _("Service images")
        ordering = ('created_at',)


class AboutUs(BaseModel):
    name = models.CharField(_("Name"), max_length=200)
    description = models.TextField(_("Description"))
    video = models.FileField(_("Video"), upload_to='videos/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("About us")
        verbose_name_plural = _("About us")


class Statistic(BaseModel):
    # client = models.PositiveIntegerField(_("Client"), default=0)
    # support = models.PositiveIntegerField(_("Support"), default=0)
    # project = models.PositiveIntegerField(_("Project"), default=0)
    # freelance = models.PositiveIntegerField(_("Freelance experience"), default=0)
    statistic_name = models.CharField(_("statistic"), max_length=150, null=True, blank=True)
    number = models.PositiveSmallIntegerField(_("Number"), default=0)

    class Meta:
        verbose_name = _("Statistic")
        verbose_name_plural = _("Statistics")

    def __str__(self):
        return f"Statistic of company -- {self.id}"


class Staff(BaseModel):
    full_name = models.CharField(_("Name"), max_length=150)
    profession = models.CharField(_("Profession"), max_length=150)
    avatar = models.ImageField(_("Avatar"), upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} -- {self.profession}"

    class Meta:
        verbose_name = _("Staff")
        verbose_name_plural = _("Staffs")


class ProjectNumber(BaseModel):
    # web_site = models.PositiveIntegerField(_("Web Site"), default=0)
    # mobile_app = models.PositiveIntegerField(_("Mobile app"), default=0)
    # crm = models.PositiveIntegerField(_("CRM"), default=0)
    # telegram_bot = models.PositiveIntegerField(_("Telegram bot"), default=0)
    project_name = models.CharField(_("Project name"), max_length=150, null=True, blank=True)
    number = models.PositiveSmallIntegerField(_("Number"), default=0)

    class Meta:
        verbose_name = _("Project number")
        verbose_name_plural = _("Project numbers")

    def __str__(self):
        return f"Completed projects -- {self.id}"


class Portfolio(BaseModel):
    name = models.CharField(_("Name"), max_length=200)
    description = models.TextField(_("Description"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolio")


class PortfolioImage(BaseModel):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, verbose_name=_("Portfolio"),
                                  related_name='images')
    image = models.ImageField(_("Image"), upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.portfolio.name} - {self.id}"

    class Meta:
        verbose_name = _("Portfolio image")
        verbose_name_plural = _("Portfolio images")
        ordering = ('created_at', )


class Sponsor(BaseModel):
    name = models.CharField(_("Sponsor"), max_length=250)
    image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsors")


class Email(BaseModel):
    _validate_phone = RegexValidator(
        regex=r"^\+?\d{9,13}$",
        message="Telefon raqamingiz 9 bilan boshlanishi va 12 ta belgidan oshmasligi lozim. "
                "Masalan: +998993451545", )
    email = models.EmailField(_("email"), validators=[EmailValidator()])
    phone_number = models.CharField(_("Phone number"), max_length=50, validators=[_validate_phone])
    message = models.CharField(_("Message"), max_length=2000)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")