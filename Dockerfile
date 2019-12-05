FROM python:3-alpine

MAINTAINER Christian

RUN mkdir /otau

WORKDIR /usr/src/app

COPY ikea.py ./

CMD [ "python", "./ikea.py" ]