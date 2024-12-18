# Generated by Django 4.0.6 on 2024-03-15 12:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('postal_code', models.CharField(max_length=20)),
                ('network', models.CharField(max_length=100)),
                ('browser', models.CharField(max_length=100)),
                ('browser_version_string', models.CharField(max_length=100)),
                ('device', models.CharField(max_length=100)),
                ('user_agent', models.TextField(max_length=256)),
                ('cookies', models.TextField(max_length=256)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
