# Generated by Django 2.0.4 on 2018-07-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_blogpage_date_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='date_published',
            field=models.DateField(blank=True, null=True, verbose_name='Date article published'),
        ),
    ]