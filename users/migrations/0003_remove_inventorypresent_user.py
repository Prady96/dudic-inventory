# Generated by Django 2.2 on 2020-01-15 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200115_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorypresent',
            name='user',
        ),
    ]
