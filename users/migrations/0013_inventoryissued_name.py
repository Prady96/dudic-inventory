# Generated by Django 2.2 on 2020-01-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200107_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryissued',
            name='name',
            field=models.CharField(default='Related_name', max_length=30),
        ),
    ]
