import csv
import pandas as pd
import ace_tools as tools
import numpy as np

# f = open('JVStuff\sample_data.csv', 'r')
# print(f.read())

def menu_choices():
    print("1.Load data from file")
    print("2.Generate synthetic data")
    print("3.Display data")
    print("4.Save data to file")
    print("5.Exit")
    choice = input("Enter your choice: ")
    return choice

def load_data():
    print("Loading data from file")
    # load data from csv file
    with open('JVStuff\sample_data.csv',mode='r') as file:
        reader=csv.reader(file)
        for row in reader:
            print(row)
    print("Data loaded successfully")
    

def check_has_header():
    print("Checking if data has header")
    # check if data has header
    with open('JVStuff\sample_data.csv',mode='r') as file:
        reader=csv.reader(file)
        header = next(reader)
        print(header)
    print("Data has header")


def handle_choices():
    choice = menu_choices()
    if choice == '1':
        # load_data()
        if check_has_header():
            print("Data has header")
        elif not check_has_header():
            print("Data does not have header")
    elif choice == '2':
        print("Generating synthetic data")
    elif choice == '3':
        print("Displaying data")
    elif choice == '4':
        print("Saving data to file")
    elif choice == '5':
        print("Exiting")
    else:
        print("Invalid choice")
        handle_choices()
        
        
import random

def generate_synthetic_data(csv_file_path, num_rows=10):
    """
    Generates synthetic data based on the structure and values of an input CSV file.
    
    Parameters:
        csv_file_path (str): Path to the input CSV file.
        num_rows (int): Number of synthetic rows to generate.
    
    Returns:
        pandas.DataFrame: DataFrame containing the synthetic data.
    """
    # Read the original data
    original_data = pd.read_csv(csv_file_path)
    
    synthetic_data = []
    
    for _ in range(num_rows):
        synthetic_row = {}
        for column in original_data.columns:
            if original_data[column].dtype == 'object':
                # For categorical/text columns, randomly pick an existing value
                synthetic_row[column] = random.choice(original_data[column].tolist())
            elif pd.api.types.is_numeric_dtype(original_data[column]):
                # For numeric columns, generate a random number within the range of existing values
                min_val, max_val = original_data[column].min(), original_data[column].max()
                synthetic_row[column] = random.uniform(min_val, max_val)
        synthetic_data.append(synthetic_row)
    
    return pd.DataFrame(synthetic_data)

# Generate synthetic data
synthetic_data = generate_synthetic_data("/mnt/data/sample_people.csv", num_rows=10)

# Display the synthetic data to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Synthetic People Data", dataframe=synthetic_data)


# main entry point for the program
__main__ = handle_choices()