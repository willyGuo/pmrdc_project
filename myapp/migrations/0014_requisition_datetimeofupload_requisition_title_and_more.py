# Generated by Django 4.0.6 on 2022-07-20 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_requisition_cfunction_requisition_cdateend_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition',
            name='dateTimeOfUpload',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='requisition',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='requisition',
            name='uploadedFile',
            field=models.FileField(default='', upload_to='Uploaded Files/'),
        ),
    ]
