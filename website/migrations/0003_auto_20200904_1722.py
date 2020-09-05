# Generated by Django 3.1 on 2020-09-04 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_olympian'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='description',
        ),
        migrations.AddField(
            model_name='candidate',
            name='email',
            field=models.EmailField(default='defaultemail@default.com', max_length=254),
        ),
    ]