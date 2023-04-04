FROM python:3.10.10

WORKDIR /code

COPY . .

RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

CMD python manage.py migrate
CMD python manage.py collectstatic --noinput
CMD gunicorn backend.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

