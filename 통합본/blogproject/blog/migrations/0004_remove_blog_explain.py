# Generated by Django 3.2.4 on 2021-06-28 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210628_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='explain',
        ),
    ]
