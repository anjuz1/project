# Generated by Django 2.0.7 on 2018-11-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply_subsidy', '0015_remove_applysubsidy_special1_consideration'),
    ]

    operations = [
        migrations.AddField(
            model_name='applysubsidy',
            name='house_typ',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='applysubsidy',
            name='mental_physical_challenge',
            field=models.CharField(default='', max_length=10),
        ),
    ]