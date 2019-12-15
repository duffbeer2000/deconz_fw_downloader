FROM python:3-alpine

RUN mkdir /otau

WORKDIR /usr/src/app

COPY *.py ./

CMD [ "python", "./fw_downloads.py" ]