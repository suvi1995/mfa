# Generated by Django 5.1.4 on 2025-01-04 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_forgetpassword_remove_signupform_auth_token'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ForgetPassword',
        ),
    ]
