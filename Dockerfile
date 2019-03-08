FROM python:3.6-alpine
COPY ./requirements.txt /home
WORKDIR /home
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
RUN pip install -r requirements.txt
COPY RssCrawler /home/RssCrawler
COPY ./script.sh /home/RssCrawler
WORKDIR /home/RssCrawler
CMD ["/bin/sh","/home/RssCrawler/script.sh"]