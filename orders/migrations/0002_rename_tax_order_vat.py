# Generated by Django 3.2.5 on 2021-07-29 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='tax',
            new_name='vat',
        ),
    ]
