# Generated by Django 2.1.7 on 2019-03-08 21:12

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('name', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('rss_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('pub_date', django_jalali.db.models.jDateTimeField()),
                ('img_url', models.TextField()),
                ('summary', models.TextField(null=True)),
                ('body', models.TextField(null=True)),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='RssItems',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('link', models.TextField()),
                ('channel_link', models.TextField(null=True)),
                ('pub_date', models.DateTimeField(null=True)),
                ('title', models.TextField(null=True)),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
    ]
