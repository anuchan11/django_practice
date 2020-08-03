from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class FakeUsers(models.Model):
    fname = models.CharField(max_length=264)
    lname = models.CharField(max_length=264)
    email = models.EmailField(max_length=264, unique=True)

    def __str__(self):
        return self.fname



class SignUp(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class UserPortfolioInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)

    def __str__(self):
        return self.user.username
