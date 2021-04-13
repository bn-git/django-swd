from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.mail import send_mail
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    ## IT action when click button
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    ## comments it's from comment class 'post' attribute, this method mean gather from comments that got approve
    def approve_comments(self):
        return self.comments.filter(approve_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk,})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
