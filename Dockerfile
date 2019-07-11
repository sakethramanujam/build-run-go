FROM python:3.6

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

RUN pip install Flask gunicorn


CMD exec gunicorn --workers 1 --threads 8 app:app