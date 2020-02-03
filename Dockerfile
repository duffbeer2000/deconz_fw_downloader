FROM python:3-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /otau

RUN pip3 install requests

WORKDIR /usr/src/app

COPY *.py ./

CMD [ "python", "./fw_downloads.py" ]