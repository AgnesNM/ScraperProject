# Generated by Django 3.2 on 2023-10-06 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScraperApp', '0007_auto_20230901_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='tshirt',
            name='defective',
            field=models.BooleanField(default=False),
        ),
    ]
