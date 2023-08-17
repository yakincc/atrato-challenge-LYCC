# Use the official Python image as the base image
FROM python:3.8.10-slim

#Set the working directory
WORKDIR /app/

RUN apt-get update \
    && apt-get clean

RUN pip install --upgrade pip
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --dev --system --deploy

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


