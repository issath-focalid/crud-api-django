
FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y python3 python3-pip libmysqlclient-dev pkg-config

WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
