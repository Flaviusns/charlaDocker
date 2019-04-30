FROM python:3.7.3

RUN mkdir servidorFlask/ && mv servidorFlask home/

RUN pip install Flask && pip install flask-cors --upgrade && pip install psycopg2

COPY main.py home/servidorFlask/
