# Generated by Django 5.0.1 on 2024-01-06 00:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_blogpost_estimated_read_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="estimated_read_time",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
