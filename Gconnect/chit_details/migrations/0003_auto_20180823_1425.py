# Generated by Django 2.0.7 on 2018-08-23 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chit_details', '0002_auto_20180823_1056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chitdetails',
            old_name='chit_details_id',
            new_name='chit_details_date',
        ),
    ]
