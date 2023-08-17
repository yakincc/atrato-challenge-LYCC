"""
This script creates a FastAPI app with two diferent endpoints: One to show a greeting message, and the other to
post and ID and return a message. This script was made for Atrato's challenge for MLOps Trainee position.

Author: Luis Yakin Carrillo Camacho
Date: 16/08/2023
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """
    Root endpoint to greet the Atrato Team.

    Returns:
        dict: Greeting message.
    """
    return {"message" : "Hello, Atrato Team!"}

@app.post("/test")
async def test(id : int):
    """
    Test endpoint to receive an ID and respond with a message.

    Parameters:
        id (int): The user's ID.

    Returns:
        dict: A response message containing the provided ID.
    """
    return {"message": f"The user has entered {id}"}