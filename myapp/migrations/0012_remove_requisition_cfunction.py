# Generated by Django 4.0.6 on 2022-07-20 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_requisition_cfunction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisition',
            name='cFunction',
        ),
    ]
