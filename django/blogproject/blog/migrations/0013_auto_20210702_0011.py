# Generated by Django 3.2.4 on 2021-07-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blog_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='bodys',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.CharField(default='', max_length=200),
        ),
    ]
