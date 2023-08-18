# SECTION 1: Use the official Python image as the base image
FROM python:3.8.10-slim

# SECTION 2: Set the working directory
WORKDIR /app/

# SECTION 3: Update the packages index and clean the temporary files
RUN apt-get update \
    && apt-get clean

#Section 4: Update pip, copy Pipfile and Pipfile.lock and install pipenv and it's packages.
RUN pip install --upgrade pip
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --dev --system --deploy

#SECTION 5: Copy all files from the root directory to the current workdir
COPY . .

#SECTION 6: Set the default command that will be executed when runing the container. This will start the API app.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


