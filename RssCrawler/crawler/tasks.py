from celery import task
from .logging import logger
import feedparser
from .models import *
from bs4 import BeautifulSoup
import requests
from django.conf import settings
from datetime import datetime
import pytz


@task
def news_parser(oid):
    try:
        item = RssItems.objects.get(pk=oid)
        response = requests.get(item.link)
        soup = BeautifulSoup(response.text, 'html.parser')
        channel_desc = settings.CHANNELS_DESCRIPTIONS[item.channel_link]
        spec = channel_desc["specifier"]

        img = soup.find('img', **{spec: channel_desc["img"]})
        title = soup.find(channel_desc["title"])
        summary = soup.find(channel_desc["summary"])
        body = soup.find(**{spec: channel_desc["body"]})
        pub_date = item.pub_date

        img_src = img.get('src') if img is not None else ""
        title_str = title.get_text(separator="\n") if title is not None else ""
        summary_str = summary.get_text(separator="\n") if summary is not None else ""
        body_str = body.get_text(separator="\n") if body is not None else ""

        obj = News(title=title_str, pub_date=pub_date, img_url=img_src, summary=summary_str, body=body_str)
        obj.save()

    except Exception:
        logger.error('an error raised in parser worker')

@task
def rss_crawler():
    logger.info('crawler task started')
    rss_urls = []
    try:
        channels = Channels.objects.all()
        rss_urls = [channel.rss_url for channel in channels]

    except BaseException:
        logger.info('maybe this object was not created yet')


    for rss in rss_urls:
        feed = feedparser.parse(rss)
        
        channel_link = feed["channel"]["link"]
        items = feed["items"]
        try:
            channel_desc = settings.CHANNELS_DESCRIPTIONS[channel_link]
        except KeyError:
            logger.error("couldn't find channel description for link {}".format(channel_link))
            continue

        for item in items:
            try:
                link = item["link"]
                pdt = datetime.strptime(item["published"], channel_desc["datetime_format"])
                dt_aware = pytz.timezone(settings.TIME_ZONE).localize(pdt)
                news_id = int(link.split('/')[channel_desc["news_index"]])
                try:
                    news = RssItems.objects.get(id=news_id)
                    continue
                except RssItems.DoesNotExist:
                    pass

                obj = RssItems(id=news_id, link=link, channel_link=channel_link,
                               pub_date=dt_aware, title=item["title"])
                obj.save()
                news_parser.apply_async((obj.id,), countdown=0)

            except Exception as e:
                logger.error("an exception raised: {}".format(e))
