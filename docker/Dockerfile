FROM python:3.8-slim


ADD ./server /home/server
WORKDIR /home/server

RUN pip3 install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/

ADD ./ui /home/ui


CMD python /home/server/app.py



