# Generated by Django 3.2.13 on 2022-05-25 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20220525_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisition',
            name='cAbility',
        ),
    ]