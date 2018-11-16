# Generated by Django 2.0.7 on 2018-07-31 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubsidyTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsidy_type_name', models.CharField(default='', max_length=50)),
                ('subsidy_type_sub_perc', models.IntegerField()),
                ('subsidy_type_self_perc', models.IntegerField()),
            ],
        ),
    ]