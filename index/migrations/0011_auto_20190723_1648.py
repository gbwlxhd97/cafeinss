# Generated by Django 2.2.3 on 2019-07-23 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_cafeinformation_other'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafeinformation',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='cafeinformation',
            name='other',
        ),
    ]
