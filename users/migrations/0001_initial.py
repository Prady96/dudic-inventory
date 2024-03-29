# Generated by Django 2.2 on 2020-01-15 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('email', models.EmailField(max_length=32, unique=True)),
                ('name', models.CharField(max_length=32)),
                ('phone_number', phone_field.models.PhoneField(max_length=31, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryIssued',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Related_name', max_length=30)),
                ('date', models.DateField(auto_now_add=True)),
                ('item_status', models.CharField(choices=[('APP', 'Approved'), ('DEC', 'Declined')], max_length=3)),
                ('comment', models.TextField(default=' ', verbose_name='Comment')),
                ('get_users', models.ManyToManyField(related_name='issued', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Inventory Issued',
            },
        ),
        migrations.CreateModel(
            name='ItemNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RoleOfUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryPresent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default='1')),
                ('date', models.DateField(auto_now_add=True)),
                ('brand', models.CharField(max_length=30)),
                ('picture', models.ImageField(blank=True, default='/Users/prady/DUDIC/dudic-inventory/inventory/static/admin/img/sample_image.svg', null=True, upload_to='inventory_thumbnails/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Categorie')),
                ('issued_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.InventoryIssued')),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.ItemNames')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Inventory Present',
            },
        ),
        migrations.AddField(
            model_name='inventoryissued',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.RoleOfUser'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.RoleOfUser'),
        ),
    ]
