# Generated by Django 3.2.12 on 2022-03-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_education_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ソフトウェア')),
                ('level', models.CharField(max_length=100, verbose_name='レベル')),
                ('percentage', models.IntegerField(verbose_name='パーセンテージ')),
            ],
        ),
        migrations.CreateModel(
            name='Technical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='テクニカル')),
                ('level', models.CharField(max_length=100, verbose_name='レベル')),
                ('percentage', models.IntegerField(verbose_name='パーセンテージ')),
            ],
        ),
    ]