# Generated by Django 3.2.8 on 2021-10-05 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('bookid1', models.CharField(max_length=30, unique=True)),
                ('bookname', models.CharField(max_length=50, unique=True)),
                ('subject', models.CharField(default='', max_length=20)),
                ('user_addbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_addbook', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IssueBook',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('current_date', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField(auto_now_add=True)),
                ('bookid2', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookid2', to='libraryApp.bookmodel')),
                ('user_issuebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_issuebook', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('student_name', models.CharField(default='', max_length=30)),
                ('phone', models.IntegerField(default=True)),
                ('user_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReturnBook',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('bookid3', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookid3', to='libraryApp.issuebook')),
                ('user_returnbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_returnbook', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
