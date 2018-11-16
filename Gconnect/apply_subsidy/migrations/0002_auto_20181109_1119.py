# Generated by Django 2.0.7 on 2018-11-09 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subsidy_elig', '0004_subsidyeligibility_subsidy_ftype'),
        ('apply_subsidy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applysubsidy',
            name='sec_elig',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='elig_sec', to='subsidy_elig.SubsidyEligibility'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applysubsidy',
            name='third_elig',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='elig_third', to='subsidy_elig.SubsidyEligibility'),
            preserve_default=False,
        ),
    ]
