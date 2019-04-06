# Generated by Django 2.2 on 2019-04-06 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openaqi_web', '0005_reading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='humidity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='reading',
            name='pm_1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='PM1'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='pm_10',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='PM10'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='pm_25',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='PM2.5'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='temperature',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
