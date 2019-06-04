# Generated by Django 2.2.1 on 2019-06-04 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190603_1630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'پروفایل کاربر', 'verbose_name_plural': 'پروفایل های کاربران'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, help_text='تصویر کاربر', null=True, upload_to='', verbose_name='تصویر کاربر'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(help_text='کاربر جنگو', on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL, verbose_name='کاربر جنگو'),
        ),
    ]
