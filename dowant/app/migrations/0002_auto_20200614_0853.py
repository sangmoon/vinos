# Generated by Django 3.0.7 on 2020-06-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='official_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='reduced_price',
            field=models.IntegerField(null=True),
        ),
    ]
