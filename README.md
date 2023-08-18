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
pip install fastapi==0.99.1
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

### Challenge 3: FastAPI. 

### Bonus Challenge: Dockerize the API.

### SQL Questions.
