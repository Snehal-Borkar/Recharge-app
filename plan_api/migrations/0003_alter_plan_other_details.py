# Generated by Django 3.2.6 on 2022-01-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan_api', '0002_auto_20220129_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='other_details',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
