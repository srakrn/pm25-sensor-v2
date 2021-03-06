# Generated by Django 2.2 on 2019-04-06 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('description', models.TextField()),
                ('secret_seed', models.CharField(editable=False, max_length=10)),
                ('secret', models.CharField(editable=False, max_length=60)),
            ],
        ),
    ]
