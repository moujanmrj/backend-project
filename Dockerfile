FROM python:3.10-alpine

WORKDIR /usr/src/app
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/app/
CMD [ "python", "manage.py", "migrate"]
CMD [ "python", "manage.py", "collectstatic", "--no-input", "--clear"]
