sleep 20 && \
python manage.py makemigrations crawler && \
python manage.py migrate && \
echo "Migration Done!"  && \
echo "from django.contrib.auth.models import User; \
    from crawler.models import Channels; \
    User.objects.filter(username='amin').exists() or \
    User.objects.create_superuser('amin', 'amin.kavosi@yahoo.com', 'Akr12345'); \
    Channels(name='irna', rss_url='http://www.irna.ir/fa/rss.aspx?kind=-1&area=0').save(); \
    Channels(name='tasnim', rss_url='https://www.tasnimnews.com/fa/rss/feed/0/8/0/%D9%85%D9%87%D9%85%D8%AA%D8%B1%DB%8C%D9%86-%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%AA%D8%B3%D9%86%DB%8C%D9%85').save() \
	" | python manage.py shell && \

python manage.py runserver 0:8000