# Generated by Django 3.2.12 on 2022-03-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_software_technical'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='youtube',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='youtube'),
        ),
    ]