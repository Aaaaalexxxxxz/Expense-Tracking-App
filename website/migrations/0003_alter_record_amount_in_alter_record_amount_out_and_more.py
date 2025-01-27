# Generated by Django 4.2.18 on 2025-01-25 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_record_birth_date_remove_record_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='amount_in',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='amount_out',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='description',
            field=models.TextField(default='', max_length=50),
        ),
    ]
