# Generated by Django 2.2 on 2019-04-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openaqi_web', '0007_reading_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='secret',
            field=models.CharField(editable=False, max_length=20),
        ),
    ]
