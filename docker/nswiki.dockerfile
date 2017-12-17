FROM python

WORKDIR /app

RUN apt -y update \
    && apt -y upgrade \
    && git clone https://github.com/RyQcan/minicms.git \
    && pip3 install -U pip \
    && pip3 install django==1.11 mysqlclient Pillow

WORKDIR /app/minicms

ONBUILD RUN git pull

RUN python checkdb.py

RUN python manage.py makemigrations \
    && python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
