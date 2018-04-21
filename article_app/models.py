from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100) # we also can use verbose_name
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True, verbose_name = "publishing date")
    thumb = models.ImageField(default="default.png", blank = True)

    # add in author later
    author = models.ForeignKey( User, default = None, on_delete = models.PROTECT)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "..."

    def jkt_time(self):
        import pytz
        # jakarta_tz = pytz.timezone('Asia/Jakarta')
        jakarta_tz = pytz.timezone('Asia/Jakarta')
        # return self.date.astimezone(jakarta_tz)
        # return self.date.tzinfo
        # return self.date.astimezone(jakarta_tz).tzinfo
        jkt_time = self.date.astimezone(jakarta_tz)

        return jkt_time
