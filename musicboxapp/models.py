from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import date, datetime

class User(models.Model):
    MAX_LENGTH = 30

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    Profile_Picture = models.ImageField(upload_to='Profile_pic', blank=True)
    Location = models.CharField(max_length=MAX_LENGTH)
    Joined = models.DateField(auto_now_add=False, default=None, null=True)
    Total_Reviews = models.IntegerField(default=0)
    Interest = models.CharField(max_length=MAX_LENGTH, default=None, null=True)
    Occupation = models.CharField(max_length=MAX_LENGTH, default=None, null=True)

    def __str__(self):
        return self.user.username

class Album(models.Model):
    TITLE_MAX_LENGTH = 30

    Title = models.CharField(max_length=TITLE_MAX_LENGTH)
    Artist = models.CharField(max_length=TITLE_MAX_LENGTH)
    Cover = models.ImageField(upload_to='Album_Cover', blank=True)
    Release = models.DateField(default=None, null=True)
    Genre = models.CharField(max_length=TITLE_MAX_LENGTH, default=None, null=True)
    Date_Of_Review = models.ForeignKey('Review', on_delete=models.CASCADE, default=None, null=True)
    Total_Reviews = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Album, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.Title

class Review(models.Model):
    Album = models.ForeignKey(Album, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Date_Of_Review = models.DateField(auto_now=False, default=None, null=True)
    Rating = models.FloatField(default=0)
    Review = models.TextField(max_length=1000)
    Title = models.CharField(max_length=40)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Album = models.ForeignKey(Album, on_delete=models.CASCADE)
    Comment = models.TextField()
    Date_Posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
