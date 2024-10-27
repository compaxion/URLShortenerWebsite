# Generated by Django 5.1.2 on 2024-10-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shortener", "0003_alter_kirrurl_shortcode"),
    ]

    operations = [
        migrations.AddField(
            model_name="kirrurl",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="kirrurl",
            name="shortcode",
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]