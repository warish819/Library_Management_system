# Generated by Django 3.2.8 on 2021-10-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0007_auto_20211005_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuebook',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
