# Generated by Django 2.2.2 on 2019-06-22 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0004_operator_api_endpoint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='to',
        ),
        migrations.AddField(
            model_name='message',
            name='to',
            field=models.CharField(default=0, help_text='Recipient of the message', max_length=15, verbose_name='Recipient of the message'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Receiver',
        ),
    ]
