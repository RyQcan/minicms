FROM python:slim

WORKDIR /app/minicms

ADD requirements.txt ./

RUN pip install -U pip \
    && pip install -r requirements.txt

CMD ["python","launch.py"]
