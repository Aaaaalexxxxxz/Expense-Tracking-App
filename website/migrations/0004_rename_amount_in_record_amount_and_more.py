# Generated by Django 4.2.18 on 2025-01-25 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_record_amount_in_alter_record_amount_out_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='amount_in',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='record',
            name='amount_out',
        ),
    ]