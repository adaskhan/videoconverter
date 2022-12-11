from django.db import models


class Convert(models.Model):
    yt_url = models.CharField(max_length=200, verbose_name='Youtube link')
    email = models.EmailField(max_length=200, verbose_name='Email')
    local_url = models.URLField(max_length=200, verbose_name='Link to download', blank=True)

    def __str__(self):
        return self.email

    def set_local_url(self, local_url):
        self.local_url = local_url
        self.save(update_fields=['local_url'])
        self.refresh_from_db(fields=['local_url'])
