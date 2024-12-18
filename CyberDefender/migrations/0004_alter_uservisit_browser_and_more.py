# Generated by Django 4.0.6 on 2024-03-15 15:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CyberDefender', '0003_alter_uservisit_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservisit',
            name='browser',
            field=models.CharField(db_column='browser', max_length=100),
        ),
        migrations.AlterField(
            model_name='uservisit',
            name='browser_version_string',
            field=models.CharField(db_column='browser_version', max_length=100),
        ),
        migrations.AlterField(
            model_name='uservisit',
            name='city',
            field=models.CharField(db_column='city', max_length=100),
        ),
        migrations.AlterField(
            model_name='uservisit',
            name='cookies',
            field=models.TextField(db_column='cookies', max_length=256),
        ),
        migrations.AlterField(
            model_name='uservisit',
            name='country',
            field=models.CharField(db_column='country', max_length=100),
        ),
        migrations.AlterField(
            model_name='uservisit',
            name='device',
            field=models.CharField(db_column='device', max_length=100),
        ),
        migrations.AlterField(
            model_name='uservisit',
            name='ip_address',
            field=models.CharField(db_column='ip_address', max_length=100),
        ),
        migrations.AlterField(
            model_name='uservisit',
            name='latitude',
            field=models.DecimalField(db_column='latitude', decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='uservisit',
            name='longitude',
            field=models.DecimalField(db_column='longitude', decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='uservisit',
            name='network',
            field=models.CharField(db_column='network', max_length=100),
        ),
        migrations.AlterField(
            model_name='uservisit',
            name='postal_code',
            field=models.CharField(db_column='postal_code', max_length=20),
        ),
        migrations.AlterField(
            model_name='uservisit',
            name='timestamp',
            field=models.DateTimeField(db_column='timestamp', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='uservisit',
            name='user_agent',
            field=models.TextField(db_column='user_agent', max_length=256),
        ),
    ]
