from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    upload_image = models.ImageField(blank=True, null=True,
                                     default='default.jpg')

    def __str__(self):
        return self.title
