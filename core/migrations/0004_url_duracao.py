# Generated by Django 3.1.4 on 2020-12-31 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201229_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='duracao',
            field=models.IntegerField(blank=True, default=5),
        ),
    ]
