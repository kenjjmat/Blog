from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # This is a one to many relationship one user can have multiple post and one post can only have one author
    # we implement this in django by using the foreignkey
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
