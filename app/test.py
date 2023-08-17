"""
This script generates a DataFrame with student information and random grades, calculates the average grades, 
and prints the resulting DataFrame. This script was made for Atrato's challenge for MLOps Trainee position.

Author: Luis Yakin Carrillo Camacho
Date: 15/08/2023
"""

import random
import pandas as pd

def generate_random_list(length : int):
    """
    Generate a list of random integer numbers between 1 and 10.

    Parameters:
        length (int): The length of the generated list.

    Returns:
        list: A list of random integer numbers of the desired lenght.
    """

    #Checking the lenght is a positive integer value
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")

    #Generating the list of random integer numbers
    list = [random.randint(1,10) for _ in range(length)]
    return list

def create_dataframe(id_list : list, name_list : list):
    """
    Create a Pandas DataFrame with three random notes for each student.

    Parameters:
        id_list (list): List of student IDs.
        name_list (list): List of student names.

    Returns:
        pandas.DataFrame: A DataFrame with student information and random notes.
    """
    #Checking if id_list and name_list are both lists
    if not isinstance(id_list, list) or not isinstance(name_list, list):
        raise ValueError("id_list and name_list must be lists.")

    #Checking that both id_list and name_list have the same size
    if len(id_list) != len(name_list):
        raise ValueError("id_list and name_list must have the same length.")

    #Generating the random lists of notes based on the size of id's list
    random_length = len(id_list)
    notes1 = generate_random_list(random_length)
    notes2 = generate_random_list(random_length)
    notes3 = generate_random_list(random_length)

    #Creating the dataframe object to store the data
    df = {'id' : id_list, 'name' : name_list, 'note1' : notes1, 'note2' : notes2, 'note3' : notes3}
    df = pd.DataFrame(df)
    return df

def calculate_average(df : pd.DataFrame):
    """
    Calculate the average of note columns and add an 'average' column to the DataFrame.

    Parameters:
        df (pandas.DataFrame): The input DataFrame containing student information and notes.

    Returns:
        pandas.DataFrame: The input DataFrame with an added 'average' column.
    """
    #Checking that the input dataframe is, in fact, a dataframe.
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")

    #Calculating the average of the notes column row-wise.
    df['avg'] = df[['note1', 'note2', 'note3']].mean(axis=1)
    return df

def test():
    """
    Test the functions by creating a DataFrame and calculating averages.
    """
    ids = [1,2,3,4,5,6]
    names= ['Juan', 'Carlos', 'Elias', 'Saúl', 'Adrian', 'Raúl']
    df = create_dataframe(ids, names)
    df = calculate_average(df)
    print(df)

    return None

if __name__ == "__main__":
    test()