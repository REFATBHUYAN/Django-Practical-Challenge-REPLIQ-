# Generated by Django 5.0.1 on 2024-02-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='condition_on_checkout',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='condition_on_return',
            field=models.TextField(blank=True, null=True),
        ),
    ]
