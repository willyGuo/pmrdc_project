# Generated by Django 4.0.6 on 2022-09-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_newsunit'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition',
            name='cStatus',
            field=models.CharField(default='processing', max_length=20),
        ),
    ]
