# Generated by Django 5.1.4 on 2025-01-06 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fluxify_post', '0003_alter_post_posted_by_alter_review_review_by'),
        ('fluxify_user', '0003_user_custome_verification_verifyed_alter_help_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
