# Generated by Django 3.2.8 on 2021-10-05 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0004_alter_issuebook_bookid2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuebook',
            old_name='current_date',
            new_name='c_date',
        ),
        migrations.RenameField(
            model_name='issuebook',
            old_name='expiry_date',
            new_name='e_date',
        ),
        migrations.AlterField(
            model_name='returnbook',
            name='bookid3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookid3', to='libraryApp.issuebook'),
        ),
    ]
