# Generated by Django 2.2 on 2020-01-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200107_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorypresent',
            name='picture',
            field=models.ImageField(blank=True, default='images/sample_image.png', null=True, upload_to='inventory_thumbnails/'),
        ),
    ]