FROM python

ARG EXP_PORT=8000

ENV LISTEN_PORT=$EXP_PORT

WORKDIR /app

ONBUILD RUN apt -y update \
        && apt -y upgrade

RUN pip3 install -U pip

WORKDIR /app/minicms

ADD requirements.txt ./

RUN pip3 install -r requirements.txt

EXPOSE $EXP_PORT

CMD ["python","launch.py"]
