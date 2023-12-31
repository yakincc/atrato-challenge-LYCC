﻿# Atrato's Challenge for MLOps Trainee application.
**Created by: Luis Yakin Carrillo Camacho**

This repository contains my solutions to the technical challenges for the MLOps Trainee position at Atrato. 
---


### Challenge 1: Virtual Environment using pipenv.
In this challenge, I set up a virtual environment for a FastAPI project using Python 3.8 and pipenv library. The goal was to create a project structure, install FastAPI version 0.99.1, and ensure the proper setup of the virtual environment.

My initial task involved the installation of pipenv, a tool I hadn't previously used. To achieve this, I executed the following command in the terminal:

```
pip install pipenv
```
Next, I have to create the virtual environment with an image of python 3.8, which I had already installed in my computer. By navigating to the project's designated folder, I executed the command:
```
pipenv --python 3.8
```
This creates a Pipfile and a Pipfile.lock, which are the files pipenv uses to controll the virtual environment. Once the virtual environment is created, the next step is to activate it, which can be done by using the command:
```
pipenv shell
```
This action activates the virtual environment within the terminal, ensuring that all scripts are executed within this environment rather than relying on the global installation. Now I can install all the required packages inside the virtual environment. 

Let's install FastAPI 's 0.99.1 version, which will be used in the next challenges. To do so, I ran the next command:
```
pipenv install fastapi==0.99.1
```
With this, the venv is all set, and we can verify that the FastAPI library is installed by checking the [Pipfile/](Pipfile/). Now, this file says that uvicorn and pandas are installed as well, but those packages will be installed later in this same challenge.

Once the venv is set, I created a new folder named "app", which will be where the scripts of the challenge will be created. Considering that I was already in the folder of the project, all i had to do was to run the command:
```
mkdir app
```
Which is Window's command to create a directort. Now the structure of the project folder looks like this, but this will be modified as we go on with the challenge:
```
atrato-challenge-LYCC/
├── Pipfile
├── Pipfile.lock
└── app/
```

### Challenge 2: Python Basics.
For the next part of the challenge, I was required to create a script named [test.py](app/test.py), which uses basic Python and the pandas library. Given a list of students' names and IDs, this script generates 3 randomn notes for every student and calculates the average of the notes, storing the results in a pandas DataFrame.

To begin with, once the test.py file was created inside the app folder, I installed the pandas library in the venv that I created before. To do this, ensuring the venv is already active, I ran the command:
```
pipenv install pandas==1.5.2
```
This installs the pandas package in the virtual environment created by pipenv, as shown in the [Pipfile](Pipfile). Once the venv was set, I wrote the script in the file [test.py](app/test.py). This script has 4 functions, each one performing a diferent task. 
* The `generate_random_list` function generates a list of random integer numbers between 1 and 10 using random library. This will help to create the random notes for each students.
* The `create_dataframe` function takes the students' names and IDs as input, generates 3 random notes for each student, and then creates a pandas.DataFrame object from the data.
* The `calculate_average` function takes the pandas.DataFrame created by the previous function, calculates the average of every student's notes and appends a new column to the dataframe named 'avg'.
* Finally, the `test` function describes the global algorithm of how the script should be executed, providing the students' names and their ids, creating the dataframe and then calculating the averages.

By executing the script, I get the following terminal output:

<picture>
<img width="500" alt="image" src="https://github.com/yakincc/atrato-challenge-LYCC/assets/107595933/490535c5-1975-4a80-8e92-f1f75ee1af87">
</picture>

Which shows that this stage of the challenge has been completed successfully. Notice that since the notes1, notes2 and notes3 columns are generated randomly, each execution of the code may lead to different results.

### Challenge 3: FastAPI. 
In this phase of the challenge, I constructed a FastAPI application within the [main.py](app/main.py) file, created an endpoint to recieve a POST request for an user's ID from the API working on the local host using uvicorn package.

To begin with, it's important to add the uvicorn package to the venv created in the first part of the challenge. To do so, I ran the following command, ensuring the venv was active:
```
pipenv install uvicorn==0.19.0
```
Once the package was installed, I created the [main.py](app/main.py) file, which has two different enpoints:
* The `root`enpoint, which method is of GET type, and simply retrieves a Hello World message as a JSON object
* The `test`enpoint, which method is of POST type, takes an integer id as an input and returns a response message containing the inputed ID.

To execute this API from my local host, I simply needed to run the following command, outside of the app directory:
```
pipenv run uvicorn app.main:app --reload
```

To test out the new API, I used Postman so I can send it requests. Since the API is runing in the localhost, all the requests must be sent to `http://127.0.0.1:8000`. A simple request of GET type to the root endpoint as shown in the next image:

<picture>
<img width="546" alt="image" src="https://github.com/yakincc/atrato-challenge-LYCC/assets/107595933/0aa5dbe5-a6f9-4add-a764-1d67c6d68bbb">
</picture>

will return the following message, with a status of 200 and in a time of 4ms as shown in the Postman interface:

<picture>
<img width="231" alt="image" src="https://github.com/yakincc/atrato-challenge-LYCC/assets/107595933/d260a491-a07f-4d0d-a72e-acb53d6736a6">
</picture>

To test out the test enpoint, I can make another request, now of POST type, as follows:

<picture>
<img width="547" alt="image" src="https://github.com/yakincc/atrato-challenge-LYCC/assets/107595933/c407866a-fe0f-4e6d-a98e-cc0755ae56bf">
</picture>

Which once sent to the API, will now retrieve the following response:

<picture>
<img width="247" alt="image" src="https://github.com/yakincc/atrato-challenge-LYCC/assets/107595933/1feec950-0047-47a0-8cf9-062c09d0e7c8">
</picture>

This shows that the API works in the localhost. Now I'll fire up a Docker container with the API, so it works in any computer withot worrying about the packages.

### Bonus Challenge: Dockerize the API.
To dockerize the API app, I was already given the [Dockerfile](Dockerfile), which contains a description of each of it's sections. I made slight modifications so I could fire the container from my own computer.

1. The first section is important, since it specifies the base image of the app. In this case I used python 3.8.10 as base image.
```
FROM python:3.8.10-slim
```
2. The second section of the code sets the working directory within the container to /app/. This means that any subsequent commands or operations will be executed relative to this directory.
```
WORKDIR /app/
```
3. The third section of the Dockerfile will update the index of the packages available to install and their versions, as well as cleaning temporary files and downloads that may exist in the system after the installation of the corresponding packages.
```
RUN apt-get update \
    && apt-get clean
```
4. The fourth section first updates pip, so we can install the required packages. Next, we copy the Pipfile and Pipfile.lock from the current Work Directory (./), and finally install `pipenv` using `pip install pipenv` as well as installing the required dependencies using `pipenv`
```
RUN pip install --upgrade pip
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --dev --system --deploy
```
5. The fifth section copies all the contents from the root directory to the current work directory within the container, so they can be accesed when executing the next section.
```
COPY . .
```
6. Finally, the sixth section defines the default command that will be executed when the container starts. This command will run the FastAPI app from the container.
```
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
Once the Dockerfile is set, we need to build the docker image. To do so, I ran the following command:
```
docker build -t myimage .
```

And then, ran the image by using the command:
```
docker run -p 8000:8000 myimage
```

Now I can use Postman to make the same requests as in Challenge 3, but with the difference that the API now runs from the container.

### SQL Questions.
For the final part of the challenge I was given the following database schema and asked to write the queries for the next questions. 

![image](https://github.com/yakincc/atrato-challenge-LYCC/assets/107595933/0c14db6c-fe56-484d-a9aa-dc5961ca8555)

Here are the questions and the corresponding queries:
1. All the orders of the customer with the customer_name = ‘Emmanuel’.
```
SELECT *
FROM Orders
INNER JOIN Customers ON Orders.customer_id = Customers.customer_id
WHERE Customers.customer_name = 'Emmanuel';
``` 

2. How many orders have the customer with customer_id = 25
```
SELECT COUNT(*)
FROM ORDERS
WHERE customer_id = 25;
```
3. Order by order_date descending, all the orders that have the customer called ‘Luis’.
```
SELECT *
FROM Orders
INNER JOIN Customers ON Orders.customer_id = Customers.customer_id
WHERE Customers.customer_name = 'Luis'
ORDER BY Orders.order_date DESC;
``` 
4. How many shipments have by order the customer with customer_id = 10.
```
SELECT COUNT(Shipments.shipment_id)
FROM Shipments
INNER JOIN Orders ON Shipments.order_id = Orders.order_id
WHERE Orders.customer_id = 10
```
To test these queries, I wrote a simple Jupyter Notebook, where I created an example database using sqlite3 as shown in [SQL-testing.ipynb](SQL-testing.ipynb). 
