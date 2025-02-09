FROM python:3-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt .
RUN apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
    && apk add --no-cache mariadb-dev \
    && python -m pip install -r requirements.txt --no-cache-dir \
    && apk --purge del .build-deps


COPY . .

CMD ["python", "main.py"]

