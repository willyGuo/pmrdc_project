# Generated by Django 3.2.13 on 2022-05-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20220524_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition',
            name='cName',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='requisition',
            name='cNumber',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='requisition',
            name='cSchedule',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='requisition',
            name='cSpecial',
            field=models.CharField(default='', max_length=100),
        ),
    ]
