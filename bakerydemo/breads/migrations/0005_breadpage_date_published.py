# Generated by Django 2.0.4 on 2018-07-11 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breads', '0004_auto_20180709_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='breadpage',
            name='date_published',
            field=models.DateField(blank=True, null=True, verbose_name='Date article published'),
        ),
    ]
