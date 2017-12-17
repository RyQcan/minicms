FROM python

WORKDIR /app

RUN apt -y update \
    && apt -y upgrade \
    && git clone https://github.com/RyQcan/minicms.git \
    && pip3 install -U pip

WORKDIR /app/minicms

RUN pip3 install -r requirements.txt

ONBUILD RUN git pull

EXPOSE 8000

CMD python checkdb.py && python manage.py runserver 0.0.0.0:8000

#CMD ["python","manage.py","runserver","0.0.0.0:8000"]
