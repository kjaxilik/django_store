# Generated by Django 2.2 on 2021-12-29 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]
