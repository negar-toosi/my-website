# Generated by Django 4.2.7 on 2023-12-10 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0014_alter_comments_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="login_require",
            field=models.BooleanField(default=False),
        ),
    ]
