FROM python

ARG EXP_PORT=8000

ENV LISTEN_PORT=$EXP_PORT

WORKDIR /app

ONBUILD RUN apt -y update \
        && apt -y upgrade \
        && pip3 install -U pip

RUN git clone https://github.com/RyQcan/minicms.git

WORKDIR /app/minicms

RUN pip3 install -r requirements.txt

ONBUILD RUN git pull

EXPOSE $EXP_PORT

CMD ["python","launch.py"]
