# Generated by Django 4.1.5 on 2023-03-10 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_verified_email_emailverification'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailverification',
            options={'verbose_name': 'Email верификация', 'verbose_name_plural': 'Email верификации'},
        ),
    ]