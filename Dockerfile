FROM python:slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y libpq-dev gcc

RUN mkdir /code
COPY . /code/
WORKDIR /code
RUN pip install -r requirements.txt

CMD hypercorn -b :$PORT core.asgi