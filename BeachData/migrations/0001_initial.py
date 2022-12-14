# Generated by Django 3.2.5 on 2022-07-22 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obs_time', models.CharField(max_length=50)),
                ('air_temp', models.FloatField()),
                ('water_temp', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_direct', models.CharField(max_length=50)),
                ('wave_height', models.FloatField()),
                ('wave_period', models.FloatField()),
                ('score', models.IntegerField()),
                ('score_msg', models.CharField(max_length=50)),
                ('beach_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'wave',
                'managed': False,
            },
        ),
    ]
