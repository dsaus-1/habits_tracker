FROM python:3.10.10

WORKDIR /code

COPY . .

RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt


