# Generated by Django 3.2.6 on 2022-01-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='data',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='sms',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='talktime',
            field=models.CharField(max_length=70, null=True),
        ),
    ]