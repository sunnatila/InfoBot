from django.db import models

from django.utils.translation import gettext_lazy as _
from .utils import upload_image_to_telegraph


class Company(models.Model):
    general_info = models.TextField(verbose_name=_('Umumiy ma\'lumot'))
    history = models.TextField(verbose_name=_("Tarix"))
    mission = models.TextField(verbose_name=_("Missiya"))
    company_vision = models.TextField(verbose_name=_("Kompaniyaning qarashlari"))
    photo = models.ImageField(upload_to='company/photos', null=True, blank=True, verbose_name=_("Rasm"))
    image_url = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, verbose_name=_("Yaratilgan Vaqt"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("Ozgartirilgan vaqt"))

    objects = models.Manager()

    def __str__(self):
        return f'{str(self.id)} - kompaniya'

    class Meta:
        verbose_name_plural = _('Kompaniyalar')
        verbose_name = _('Kompaniya ')
        db_table = 'companies'
        ordering = ['created_at']

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.upload_image()
        super().save(*args, **kwargs)

    def upload_image(self):
        self.image_url = upload_image_to_telegraph(self.photo)
        self.save()


class Service(models.Model):
    service = models.TextField(verbose_name=_("Servis xizmati"))
    product = models.TextField(verbose_name=_("Mahsulot"))

    objects = models.Manager()

    def __str__(self):
        return f'{str(self.id)} - servis'

    class Meta:
        verbose_name_plural = _('Servislar')
        verbose_name = _('Servis ')
        db_table = 'services'


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name=_("Sarlavha"))
    body = models.TextField(verbose_name=_("Batafsil ma'lumot"))
    image = models.ImageField(upload_to='news/photos', null=True, blank=True, verbose_name=_("Rasm"))
    image_url = models.CharField(max_length=150, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, verbose_name=_("Yaratilgan Vaqt"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("Ozgartirilgan vaqt"))

    objects = models.Manager()

    def __str__(self):
        return f'{str(self.id)} - yangilik'

    class Meta:
        verbose_name_plural = _('Yangiliklar')
        verbose_name = _('Yangilik ')
        db_table = 'news'

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.upload_image()
        super().save(*args, **kwargs)

    def upload_image(self):
        self.image_url = upload_image_to_telegraph(self.image)
        self.save()


class Investor(models.Model):
    financial_info = models.TextField(verbose_name=_("Moliyaviy ma'lumot"))
    reports = models.TextField(verbose_name=_("Hisobot"))
    future_plan = models.TextField(verbose_name=_("Kelajak rejalari"))
    contact_info = models.CharField(max_length=250, verbose_name=_("Aloqa ma'lumoti"))
    image = models.ImageField(upload_to='investors/photos', null=True, blank=True, verbose_name=_("Rasm"))
    image_url = models.CharField(max_length=150, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, verbose_name=_("Yaratilgan Vaqt"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("Ozgartirilgan vaqt"))

    objects = models.Manager()

    def __str__(self):
        return f'{str(self.id)} - investor'

    class Meta:
        verbose_name_plural = _('Moliyaviy ma\'lumotlar')
        verbose_name = _('Moliyaviy ma\'lumot haqida ')
        db_table = 'investors'

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.upload_image()
        super().save(*args, **kwargs)

    def upload_image(self):
        self.image_url = upload_image_to_telegraph(self.image)
        self.save()


class InvestApplication(models.Model):
    fullname = models.CharField(max_length=47, verbose_name=_("To'liq ismingiz"))
    phone = models.CharField(max_length=50, verbose_name=_("Telefon raqam"))
    advice = models.TextField(verbose_name=_("Batafsil maslahat"))
    create_at = models.DateField(auto_now_add=True, verbose_name=_("Yaratilgan Vaqt"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("Ozgartirilgan vaqt"))

    objects = models.Manager()

    def __str__(self):
        return f'{str(self.id)} - investor arizasi'

    class Meta:
        verbose_name_plural = _('Investorlar arizalari')
        verbose_name = _('Ariza ')
        db_table = 'invest_applications'


class Partner(models.Model):
    partnership_opportunities = models.CharField(max_length=1000, verbose_name=_("Hamkorlik imkoniyatlari"))
    partnership_programs = models.CharField(max_length=1000, verbose_name=_("Hamkorlik dasturlari"))
    conditions = models.CharField(max_length=1000, verbose_name=_("Shartlar"))
    contact_info = models.CharField(max_length=1000, verbose_name=_("Aloqa ma'lumotlari"))
    image = models.ImageField(upload_to='partner/photos', null=True, blank=True, verbose_name=_("Rasm"))
    image_url = models.CharField(max_length=150, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, verbose_name=_("Yaratilgan Vaqt"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("Ozgartirilgan vaqt"))

    objects = models.Manager()

    def __str__(self):
        return f'{str(self.id)} - hamkor'

    class Meta:
        verbose_name_plural = _('Hamkorlikning afzalliklari')
        verbose_name = _('Hamkorlikning afzalliklarini ')
        db_table = 'partners'

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.upload_image()
        super().save(*args, **kwargs)

    def upload_image(self):
        self.image_url = upload_image_to_telegraph(self.image)
        self.save()


class PartnershipApplication(models.Model):
    fullname = models.CharField(max_length=70, verbose_name=_('To\'liq ismingiz'))
    phone = models.CharField(max_length=50, verbose_name=_("Telefon raqam"))
    advice = models.TextField(verbose_name=_("Batafsil maslahat"))
    create_at = models.DateField(auto_now_add=True, verbose_name=_("Yaratilgan Vaqt"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("Ozgartirilgan vaqt"))

    objects = models.Manager()

    def __str__(self):
        return f'{str(self.id)} - hamkor arizasi'

    class Meta:
        verbose_name_plural = _('Hamkorlar arizalari')
        verbose_name = _('Ariza ')
        db_table = 'partner_applications'


class ContactInformation(models.Model):
    company_address = models.CharField(max_length=500, verbose_name=_("Kompaniya manzillari"))
    phone_number = models.CharField(max_length=500, verbose_name=_("Telefon raqamlar"))
    email = models.CharField(max_length=500, verbose_name=_("Elektron pochta"))
    social_networks = models.CharField(max_length=500, verbose_name=_("Ijtimoiy tarmoqlar"))
    create_at = models.DateField(auto_now_add=True, verbose_name=_("Yaratilgan Vaqt"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("Ozgartirilgan vaqt"))

    objects = models.Manager()

    def __str__(self):
        return f'{str(self.id)} - kontakt'

    class Meta:
        verbose_name_plural = _('Kontaktlar')
        verbose_name = _('Kontakt ')
        db_table = 'contacts'


class FAQ(models.Model):
    question = models.TextField(verbose_name=_("Savol"))
    answer = models.TextField(verbose_name=_("Javob"))
    create_at = models.DateField(auto_now_add=True, verbose_name=_("Yaratilgan Vaqt"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("Ozgartirilgan vaqt"))

    objects = models.Manager()

    def __str__(self):
        return f'{str(self.id)} - savol'

    class Meta:
        verbose_name_plural = _('Savolar')
        verbose_name = _('Savol ')
        db_table = 'questions'

