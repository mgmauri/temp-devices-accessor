FROM python:3.7-slim

WORKDIR /app/
# Install Poetry
RUN python -m pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update

RUN apt-get install gcc -y \
    && apt-get install -y tzdata \
    && apt-get clean

RUN pip install -r /app/requirements.txt

COPY ./app /app
ENV PYTHONPATH=/app
EXPOSE 8000
