# Generated by Django 2.2 on 2020-01-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200116_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorypresent',
            name='brand',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
