FROM python:3.6-jessie
COPY ./requirements.txt /home
WORKDIR /home
RUN apt-get update && \
    apt-get install -y netcat tzdata && \
    pip install -r requirements.txt

COPY RssCrawler /home/RssCrawler
COPY ./script.sh /home/RssCrawler
WORKDIR /home/RssCrawler
CMD ["/bin/sh","/home/RssCrawler/script.sh"]