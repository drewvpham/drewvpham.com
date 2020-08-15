from django.db import models
from posts.models import Category, Post
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
User = get_user_model()


class Project(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, blank=True, null=True)
    view_count = models.IntegerField(default=0)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    slug = models.SlugField()
    url = models.CharField(max_length=50)

    # check the below
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={
            'slug': self.slug
        })

    def get_update_url(self):
        return reverse('project-update', kwargs={
            'slug': self.slug
        })

    def get_delete_url(self):
        return reverse('project-delete', kwargs={
            'slug': self.slug
        })
