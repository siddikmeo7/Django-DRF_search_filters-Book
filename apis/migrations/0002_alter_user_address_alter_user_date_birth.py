# Generated by Django 5.0 on 2024-11-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
