# Generated by Django 4.1.5 on 2023-01-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishName', models.CharField(max_length=30)),
                ('dishPrice', models.CharField(max_length=10)),
                ('dishDescription', models.CharField(max_length=200)),
                ('dishPicture', models.CharField(max_length=30)),
            ],
        ),
    ]