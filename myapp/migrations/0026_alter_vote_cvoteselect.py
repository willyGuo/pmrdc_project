# Generated by Django 4.0.6 on 2022-09-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_vote_cvoteselect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='cVoteselect',
            field=models.CharField(default='Null', max_length=30),
        ),
    ]