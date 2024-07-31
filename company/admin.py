from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import (
    News,
    PartnershipApplication,
    Partner,
    InvestApplication,
    Investor,
    ContactInformation,
    Company,
    Service,
    FAQ
)
from . import translations


@admin.register(News)
class NewsAdmin(TabbedTranslationAdmin):
    list_display = ('title',)


@admin.register(PartnershipApplication)
class PartnershipApplicationAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Partner)
class PartnerAdmin(TabbedTranslationAdmin):
    list_display = ('id',)


@admin.register(InvestApplication)
class InvestApplicationAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Investor)
class InvestorAdmin(TabbedTranslationAdmin):
    list_display = ('id',)


@admin.register(ContactInformation)
class ContactInformationAdmin(TabbedTranslationAdmin):
    list_display = ('id',)


@admin.register(Company)
class CompanyAdmin(TabbedTranslationAdmin):
    list_display = ('id',)


@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
    list_display = ('id',)


@admin.register(FAQ)
class FAQAdmin(TabbedTranslationAdmin):
    list_display = ('id',)


