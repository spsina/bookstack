# Generated by Django 2.2.1 on 2019-06-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_auto_20190603_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionnaire',
            old_name='title',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_selected',
            field=models.BooleanField(default=False, help_text='is an answer selected or not', verbose_name='is selected'),
        ),
    ]
