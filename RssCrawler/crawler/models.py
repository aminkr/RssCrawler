from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.utils.html import format_html

# Create your models here.


class Channels(models.Model):
    name = models.CharField(max_length=60, primary_key=True)
    rss_url = models.TextField()

    class Meta:
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'


class RssItems(models.Model):
    id = models.IntegerField(primary_key=True)
    link = models.TextField(null=False)
    channel_link = models.TextField(null=True)
    pub_date = models.DateTimeField(null=True)
    title = models.TextField(null=True)

    class Meta:
        ordering = ["pub_date"]

    def __str__(self):
        return '(%s)' % (self.title)


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    pub_date = jmodels.jDateTimeField(null=False)
    img_url = models.TextField(null=False)
    summary = models.TextField(null=True)
    body = models.TextField(null=True)

    class Meta:
        ordering = ["pub_date"]
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def short_body(self):
        if len(self.body) > 100:
            return self.body[0:100] + u' ...'
        else:
            return self.body

    def img_src(self):
        return format_html(
            '<a href="{}">{}</a>',
            self.img_url,
            "دیدن"
        )