# Generated by Django 5.1.4 on 2024-12-30 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_id', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=10)),
                ('pin_code', models.CharField(max_length=6)),
                ('adress', models.TextField()),
                ('profile_photo', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_image', models.ImageField(upload_to='media/')),
                ('report_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reports', to='fluxify_user.user')),
            ],
        ),
        migrations.CreateModel(
            name='help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('help_image', models.ImageField(upload_to='media/')),
                ('help_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='help', to='fluxify_user.user')),
            ],
        ),
        migrations.CreateModel(
            name='verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_id', models.CharField(max_length=200)),
                ('x_id', models.CharField(max_length=200)),
                ('youtube_name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='verificatio', to='fluxify_user.user')),
            ],
        ),
    ]
