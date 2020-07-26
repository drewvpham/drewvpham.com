from django.db import models
from posts.models import Category
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # content = HTMLField()
    # comment_count = models.IntegerField(default = 0)
    # view_count = models.IntegerField(default = 0)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={
            'pk': self.pk
        })

    def get_update_url(self):
        return reverse('project-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('project-delete', kwargs={
            'pk': self.pk
        })
