# Generated by Django 3.2.8 on 2021-10-05 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0006_issuebook_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuebook',
            name='c_date',
        ),
        migrations.RemoveField(
            model_name='issuebook',
            name='e_date',
        ),
        migrations.RemoveField(
            model_name='issuebook',
            name='name',
        ),
    ]
