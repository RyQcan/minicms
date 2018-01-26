FROM python:alpine

ARG EXP_PORT=8000

ENV LISTEN_PORT=$EXP_PORT

RUN pip install -U pip

WORKDIR /app/minicms

ADD requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE $EXP_PORT

CMD ["python","launch.py"]
