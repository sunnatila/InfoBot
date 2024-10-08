# Generated by Django 5.0.7 on 2024-07-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_vision_ru',
            field=models.TextField(null=True, verbose_name='Kompaniyaning qarashlari'),
        ),
        migrations.AddField(
            model_name='company',
            name='company_vision_uz',
            field=models.TextField(null=True, verbose_name='Kompaniyaning qarashlari'),
        ),
        migrations.AddField(
            model_name='company',
            name='general_info_ru',
            field=models.TextField(null=True, verbose_name="Umumiy ma'lumot"),
        ),
        migrations.AddField(
            model_name='company',
            name='general_info_uz',
            field=models.TextField(null=True, verbose_name="Umumiy ma'lumot"),
        ),
        migrations.AddField(
            model_name='company',
            name='history_ru',
            field=models.TextField(null=True, verbose_name='Tarix'),
        ),
        migrations.AddField(
            model_name='company',
            name='history_uz',
            field=models.TextField(null=True, verbose_name='Tarix'),
        ),
        migrations.AddField(
            model_name='company',
            name='mission_ru',
            field=models.TextField(null=True, verbose_name='Missiya'),
        ),
        migrations.AddField(
            model_name='company',
            name='mission_uz',
            field=models.TextField(null=True, verbose_name='Missiya'),
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='company_address_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Kompaniya manzillari'),
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='company_address_uz',
            field=models.CharField(max_length=500, null=True, verbose_name='Kompaniya manzillari'),
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='email_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Elektron pochta'),
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='email_uz',
            field=models.CharField(max_length=500, null=True, verbose_name='Elektron pochta'),
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='phone_number_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Telefon raqamlar'),
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='phone_number_uz',
            field=models.CharField(max_length=500, null=True, verbose_name='Telefon raqamlar'),
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='social_networks_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Ijtimoiy tarmoqlar'),
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='social_networks_uz',
            field=models.CharField(max_length=500, null=True, verbose_name='Ijtimoiy tarmoqlar'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ru',
            field=models.TextField(null=True, verbose_name='Javob'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_uz',
            field=models.TextField(null=True, verbose_name='Javob'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ru',
            field=models.TextField(null=True, verbose_name='Savol'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_uz',
            field=models.TextField(null=True, verbose_name='Savol'),
        ),
        migrations.AddField(
            model_name='investor',
            name='contact_info_ru',
            field=models.CharField(max_length=250, null=True, verbose_name="Aloqa ma'lumoti"),
        ),
        migrations.AddField(
            model_name='investor',
            name='contact_info_uz',
            field=models.CharField(max_length=250, null=True, verbose_name="Aloqa ma'lumoti"),
        ),
        migrations.AddField(
            model_name='investor',
            name='financial_info_ru',
            field=models.TextField(null=True, verbose_name="Moliyaviy ma'lumot"),
        ),
        migrations.AddField(
            model_name='investor',
            name='financial_info_uz',
            field=models.TextField(null=True, verbose_name="Moliyaviy ma'lumot"),
        ),
        migrations.AddField(
            model_name='investor',
            name='future_plan_ru',
            field=models.TextField(null=True, verbose_name='Kelajak rejalari'),
        ),
        migrations.AddField(
            model_name='investor',
            name='future_plan_uz',
            field=models.TextField(null=True, verbose_name='Kelajak rejalari'),
        ),
        migrations.AddField(
            model_name='investor',
            name='reports_ru',
            field=models.TextField(null=True, verbose_name='Hisobot'),
        ),
        migrations.AddField(
            model_name='investor',
            name='reports_uz',
            field=models.TextField(null=True, verbose_name='Hisobot'),
        ),
        migrations.AddField(
            model_name='news',
            name='body_ru',
            field=models.TextField(null=True, verbose_name="Batafsil ma'lumot"),
        ),
        migrations.AddField(
            model_name='news',
            name='body_uz',
            field=models.TextField(null=True, verbose_name="Batafsil ma'lumot"),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='partner',
            name='conditions_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Shartlar'),
        ),
        migrations.AddField(
            model_name='partner',
            name='conditions_uz',
            field=models.CharField(max_length=1000, null=True, verbose_name='Shartlar'),
        ),
        migrations.AddField(
            model_name='partner',
            name='contact_info_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name="Aloqa ma'lumotlari"),
        ),
        migrations.AddField(
            model_name='partner',
            name='contact_info_uz',
            field=models.CharField(max_length=1000, null=True, verbose_name="Aloqa ma'lumotlari"),
        ),
        migrations.AddField(
            model_name='partner',
            name='partnership_opportunities_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Hamkorlik imkoniyatlari'),
        ),
        migrations.AddField(
            model_name='partner',
            name='partnership_opportunities_uz',
            field=models.CharField(max_length=1000, null=True, verbose_name='Hamkorlik imkoniyatlari'),
        ),
        migrations.AddField(
            model_name='partner',
            name='partnership_programs_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Hamkorlik dasturlari'),
        ),
        migrations.AddField(
            model_name='partner',
            name='partnership_programs_uz',
            field=models.CharField(max_length=1000, null=True, verbose_name='Hamkorlik dasturlari'),
        ),
        migrations.AddField(
            model_name='service',
            name='product_ru',
            field=models.TextField(null=True, verbose_name='Mahsulot'),
        ),
        migrations.AddField(
            model_name='service',
            name='product_uz',
            field=models.TextField(null=True, verbose_name='Mahsulot'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_ru',
            field=models.TextField(null=True, verbose_name='Servis xizmati'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_uz',
            field=models.TextField(null=True, verbose_name='Servis xizmati'),
        ),
    ]
