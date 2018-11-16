# Generated by Django 2.0.7 on 2018-08-22 09:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_date', models.DateField(default=datetime.date.today)),
                ('meeting_time', models.TimeField()),
                ('meeting_agenda', models.CharField(default='', max_length=200)),
                ('meeting_status', models.IntegerField(default=0)),
                ('meeting_decisions', models.CharField(default='', max_length=500)),
                ('place_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.Place')),
            ],
        ),
    ]