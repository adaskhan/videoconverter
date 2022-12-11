from django.db import models


class Convert(models.Model):
    yt_url = models.CharField(max_length=200, verbose_name='Youtube link')
    email = models.EmailField(max_length=200, verbose_name='Email')

    def __str__(self):
        return self.email
