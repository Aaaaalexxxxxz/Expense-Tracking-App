# Generated by Django 4.2.18 on 2025-02-05 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_record_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='monthly_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('income', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('expense', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='next_occurance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='recurrance',
            field=models.CharField(choices=[('Once', 'Once'), ('Weekly', 'Weekly'), ('Biweekly', 'Biweekly'), ('Monthly', 'Monthly')], default='Once', max_length=10),
        ),
    ]
