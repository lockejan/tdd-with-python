# pull official base image
# FROM python:3.9.6-alpine
FROM python:3.9.13-bullseye

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
# install dependencies
COPY ./requirements.txt .
COPY ./requirements-dev.txt .
RUN pip install -r requirements-dev.txt

# copy project
COPY . .

CMD [ "python", "manage.py","runserver","0.0.0.0:8000" ]
