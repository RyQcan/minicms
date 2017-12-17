FROM python

ARG EXP_PORT=8000

ENV LISTEN_PORT=$EXP_PORT

WORKDIR /app

RUN apt -y update \
    && apt -y upgrade \
    && git clone https://github.com/RyQcan/minicms.git \
    && pip3 install -U pip

WORKDIR /app/minicms

RUN pip3 install -r requirements.txt

ONBUILD RUN git pull

EXPOSE $EXP_PORT

#CMD python checkdb.py && python manage.py runserver 0.0.0.0:8000

CMD ["python","launch.py"]
