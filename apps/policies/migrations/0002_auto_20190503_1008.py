# Generated by Django 2.2 on 2019-05-03 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedulepolicy',
            options={'verbose_name': 'Schedule policy', 'verbose_name_plural': 'Schedule policies'},
        ),
    ]