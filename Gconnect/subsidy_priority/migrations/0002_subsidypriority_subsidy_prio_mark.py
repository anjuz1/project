# Generated by Django 2.0.7 on 2018-07-31 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subsidy_priority', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsidypriority',
            name='subsidy_prio_mark',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]