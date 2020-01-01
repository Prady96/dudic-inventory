# Generated by Django 2.2 on 2019-12-29 12:12

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191228_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryissued',
            name='get_users',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='get_user_type', chained_model_field='user_type', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
