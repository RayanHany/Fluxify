# Generated by Django 5.1.4 on 2025-01-06 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fluxify_post', '0002_rename_catagory_post_category_post_status'),
        ('fluxify_user', '0003_user_custome_verification_verifyed_alter_help_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='fluxify_user.user_custome'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='fluxify_user.user_custome'),
        ),
    ]
