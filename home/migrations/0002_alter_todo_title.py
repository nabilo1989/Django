# Generated by Django 4.0.1 on 2022-01-19 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
