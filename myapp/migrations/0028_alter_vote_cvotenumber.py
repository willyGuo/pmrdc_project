# Generated by Django 4.0.6 on 2022-09-30 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_alter_vote_cvoteselect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='cVotenumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.requisition'),
        ),
    ]
