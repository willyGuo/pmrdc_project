# Generated by Django 4.0.6 on 2022-07-20 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_requisition_cdateend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='cdateend',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='cdatestart',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
