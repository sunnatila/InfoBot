# Generated by Django 5.0.7 on 2024-07-29 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tguser',
            options={'verbose_name': 'Telegram foydalanuvchi ', 'verbose_name_plural': 'Telegram foydalanuvchilar'},
        ),
    ]