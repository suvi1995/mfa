# Generated by Django 5.1.4 on 2025-01-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_rename_password1_signupform_conform_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupform',
            old_name='Conform_password',
            new_name='Conform_Password',
        ),
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='acb46a', max_length=6),
        ),
    ]
