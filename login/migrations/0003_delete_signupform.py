# Generated by Django 5.1.4 on 2025-01-03 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_signupform_delete_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUpForm',
        ),
    ]
