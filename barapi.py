import pandas as pd
import matplotlib.pyplot as plt

def read_csv_data(file_path):
    """Reads data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing the data from the CSV file.
    """

    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None

def create_barplot(data, x_label, y_label, title):
    """Creates a barplot based on the given data.

    Args:
        data (pandas.DataFrame): The data to be plotted.
        x_label (str): The label for the x-axis.
        y_label (str): The label for the y-axis.
        title (str): The title of the plot.
    """

    plt.figure(figsize=(10, 6))
    plt.bar(data[x_label], data[y_label], color='skyblue')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

# Replace 'your_data.csv' with the actual path to your CSV file
file_path = 'data.csv'

try:
    df = read_csv_data(file_path)

    if df is not None:
        # Assuming the CSV file has columns named 'Category' and 'Value'
        x_label = 'Category'
        y_label = 'Value'
        title = 'Bar Plot from CSV Data'

        create_barplot(df, x_label, y_label, title)
except FileNotFoundError:
    print("Error: File not found.")