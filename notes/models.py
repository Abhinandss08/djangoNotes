from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True,blank=True)
    upload_image = models.ImageField(blank=True, null=True,
                                     default='default.jpg')

    def __str__(self):
        return self.title
