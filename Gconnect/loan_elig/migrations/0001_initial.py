# Generated by Django 2.0.7 on 2018-10-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanEligibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_elig_name', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
