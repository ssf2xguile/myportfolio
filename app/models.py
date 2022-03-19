from email.policy import default
from django.db import models

class Profile(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
    name = models.CharField('名前', max_length=100)
    job = models.TextField('仕事')
    youtube = models.CharField('youtube', max_length=100, null=True, blank=True)
    github = models.CharField('github', max_length=100, null=True, blank=True)
    twitter = models.CharField('twitter', max_length=100, null=True, blank=True)
    facebook = models.CharField('facebook', max_length=100, null=True, blank=True)
    instagram = models.CharField('instagram', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
    subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')

    def __str__(self):
        return self.name

class Work(models.Model):
    """作品用モデル"""
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField(default='/images/django-img.svg',upload_to="images", verbose_name='イメージ画像')
    thumbnail = models.ImageField(default='/images/django-thumbnail.png',upload_to="images", verbose_name='サムネイル', null='True', blank='True')
    skill = models.CharField('スキル', max_length=100)
    url = models.CharField('URL', max_length=100, null='True', blank='True')
    created = models.DateField('作成日')
    description = models.TextField('説明')

    def __str__(self):
        return self.title

class Experience(models.Model):
    """職歴用モデル"""
    occupation = models.CharField('職種', max_length=100)
    company = models.CharField('会社', max_length=100)
    description = models.TextField('説明')
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.occupation

class Education(models.Model):
    """学歴用モデル"""
    school = models.CharField('学校', max_length=100)
    course = models.CharField('学部学科', max_length=100)
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.course
    
class Software(models.Model):
    """ソフトウェア用モデル"""
    name = models.CharField('ソフトウェア', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name



class Technical(models.Model):
    """スキル用モデル"""
    name = models.CharField('テクニカル', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name