# Generated by Django 3.2.22 on 2023-11-23 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]
