from modeltranslation.translator import register, TranslationOptions, translator
from .models import (
    News,
    Partner,
    Investor,
    ContactInformation,
    Company,
    Service,
    FAQ
)


@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ['general_info', 'history', 'mission', 'company_vision']


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ['service', 'product']


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ['title', 'body']


@register(Investor)
class InvestorTranslationOptions(TranslationOptions):
    fields = ['financial_info', 'reports', 'future_plan', 'contact_info']


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ['partnership_opportunities', 'partnership_programs', 'conditions', 'contact_info']


@register(ContactInformation)
class ContactInformationTranslationOptions(TranslationOptions):
    fields = ['company_address', 'phone_number', 'email', 'social_networks']


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ['question', 'answer']
