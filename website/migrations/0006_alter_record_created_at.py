# Generated by Django 4.2.18 on 2025-01-25 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_record_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
