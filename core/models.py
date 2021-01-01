from django.db import models
from hashlib import md5
from django.utils import timezone
from django.core.validators import URLValidator

#validators=[URLValidator()]
class Url(models.Model):
    full_url = models.URLField(unique=True)
    short_url = models.TextField(unique=True, blank=True)
    clicks = models.IntegerField(default=0, blank=True)
    created = models.DateTimeField(default=timezone.now, blank=True)
    duracao = models.IntegerField(default=5, blank=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not 'http://' in self.full_url and not 'https://' in self.full_url:
            self.full_url = 'http://'+self.full_url
        if not self.id:
            self.short_url = md5(self.full_url.encode()).hexdigest()[:10]

        return super(Url, self).save(*args, **kwargs)

    def __str__(self):
        return self.short_url