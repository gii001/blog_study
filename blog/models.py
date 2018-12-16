from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    def __str__(self):
        return self.tag_name


class Post(models.Model):
    post_title = models.CharField(max_length=70)
    post_body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)
    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})