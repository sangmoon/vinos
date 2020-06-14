# Generated by Django 3.0.7 on 2020-06-14 09:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200614_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wine',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='wine',
            name='shop',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
