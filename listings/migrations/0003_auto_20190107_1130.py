# Generated by Django 2.1.4 on 2019-01-07 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20190105_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='realtors',
            new_name='realtor',
        ),
    ]
