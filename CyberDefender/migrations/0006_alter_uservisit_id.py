# Generated by Django 5.0.3 on 2024-03-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CyberDefender", "0005_auto_20240318_2029"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uservisit",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]