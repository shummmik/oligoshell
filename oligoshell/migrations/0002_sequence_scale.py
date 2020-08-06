# Generated by Django 3.1 on 2020-08-06 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oligoshell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequence',
            name='scale',
            field=models.CharField(choices=[('50', '50 nmol'), ('200', '200 nmol'), ('1000', '1 umol')], default='50', max_length=20),
        ),
    ]
