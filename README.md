# Atrato's Challenge for MLOps Trainee application.
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
Which is Window's command to create a directort. Now the structure of the project folder looks like this, but this will be modifyied as we go on with the challenge:
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
<img width="248" alt="image" src="https://github.com/yakincc/atrato-challenge-LYCC/assets/107595933/490535c5-1975-4a80-8e92-f1f75ee1af87">

Which shows that this stage of the challenge has been completed successfully. 

### Challenge 3: FastAPI. 



### Bonus Challenge: Dockerize the API.

### SQL Questions.
