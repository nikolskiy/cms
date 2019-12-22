FROM python:3.7-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
RUN mkdir api
COPY ./ /api

# set work directory
WORKDIR /api/

RUN pip3 install -r requirements.txt
RUN python3 manage.py migrate

EXPOSE 8080

# doesn't serve static files
#CMD ["gunicorn", "-b", "0.0.0.0:8080",  "main.wsgi"]

CMD ["python3", "manage.py", "runserver",  "0.0.0.0:8080"]
