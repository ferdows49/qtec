# Generated by Django 3.1.7 on 2021-03-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s_history',
            name='time',
            field=models.DateTimeField(),
        ),
    ]