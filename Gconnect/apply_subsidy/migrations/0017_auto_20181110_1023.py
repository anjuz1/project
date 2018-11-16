# Generated by Django 2.0.7 on 2018-11-10 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subsidy_elig', '0004_subsidyeligibility_subsidy_ftype'),
        ('apply_subsidy', '0016_auto_20181110_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='applysubsidy',
            name='adhar_card_no',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='applysubsidy',
            name='first_elig',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='subsidy_elig.SubsidyEligibility'),
        ),
        migrations.AddField(
            model_name='applysubsidy',
            name='ration_card_no',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='applysubsidy',
            name='voter_id',
            field=models.CharField(default='', max_length=20),
        ),
    ]