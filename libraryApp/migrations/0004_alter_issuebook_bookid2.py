# Generated by Django 3.2.8 on 2021-10-05 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0003_auto_20211005_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='bookid2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookid2', to='libraryApp.bookmodel'),
        ),
    ]