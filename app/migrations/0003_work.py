# Generated by Django 3.2.12 on 2022-03-17 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_profile_linkedin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('image', models.ImageField(upload_to='images', verbose_name='イメージ画像')),
                ('thumbnail', models.ImageField(blank='True', null='True', upload_to='images', verbose_name='サムネイル')),
                ('skill', models.CharField(max_length=100, verbose_name='スキル')),
                ('url', models.CharField(blank='True', max_length=100, null='True', verbose_name='URL')),
                ('created', models.DateField(verbose_name='作成日')),
                ('description', models.TextField(verbose_name='説明')),
            ],
        ),
    ]
