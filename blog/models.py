from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now
from ckeditor.fields import RichTextField
# Create your models here.

# Post model, creates a post with title, content, author, time (view count and slug)
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.CharField(max_length=40)
    views = models.IntegerField(default=0)
    slug = models.CharField(max_length=140)
    timeStamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' by ' + self.author

# Comment and reply model, makes comment with ref to user, post and parent comment (timestamp and reply)
class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + ".. By: " + self.user.username