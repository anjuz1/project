# Generated by Django 2.0.7 on 2018-11-09 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('housename', '0005_auto_20180925_1333'),
        ('apply_subsidy', '0007_applysubsidy_applicant_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='applysubsidy',
            name='Address_hname',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='housename.Housename'),
            preserve_default=False,
        ),
    ]