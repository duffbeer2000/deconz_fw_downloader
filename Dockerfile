FROM python:3-alpine

RUN mkdir /otau

WORKDIR /usr/src/app

COPY ikea.py ./

CMD [ "python", "./fw_downloads.py" ]