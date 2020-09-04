# Generated by Django 3.1 on 2020-09-04 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Olympian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('school', models.CharField(max_length=15)),
                ('picture', models.ImageField(upload_to='olympians')),
                ('participations', models.CharField(max_length=50)),
                ('languages', models.CharField(max_length=255)),
                ('career', models.CharField(max_length=200)),
            ],
        ),
    ]
