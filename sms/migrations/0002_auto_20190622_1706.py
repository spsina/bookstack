# Generated by Django 2.2.2 on 2019-06-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A name for the operator', max_length=255, verbose_name='Operator Name')),
                ('username', models.CharField(help_text='User name given by operator', max_length=255, verbose_name='Username')),
                ('password', models.CharField(help_text='Password given by operator', max_length=255, verbose_name='گذرواژه')),
                ('sender', models.CharField(help_text='The operator phone number', max_length=15, verbose_name='Sender Phone Number')),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='operator',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AlterField(
            model_name='message',
            name='last_try',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
