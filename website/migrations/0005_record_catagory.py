# Generated by Django 4.2.18 on 2025-01-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_rename_amount_in_record_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='catagory',
            field=models.CharField(default='', max_length=20),
        ),
    ]
