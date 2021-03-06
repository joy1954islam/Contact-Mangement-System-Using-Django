# Generated by Django 3.0b1 on 2020-06-21 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('nickname', models.TextField(blank=True, max_length=64, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('P', 'Prefer not to answer')], max_length=8)),
                ('bio', models.TextField(blank=True, max_length=1024, null=True)),
                ('profile_image', models.ImageField(blank=True, default='default-avatar.png', null=True, upload_to='Contact_profile/')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
