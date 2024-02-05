import pandas as pd

def convert_flat_file(input_path, output_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_path, header=None)

    # Add headers, named values Header 1, Header 2, etc., finishing with Header 20
    headers = [f'Header {i}' for i in range(1, 21)]

    # Ensure the DataFrame has the correct number of columns
    df.columns = headers[:len(df.columns)]

    # For all rows with a first column value of L
    mask = df['Header 1'] == 'L'

    # Move columns 6 and 9 to columns 19 and 20 (This is the SKU and Qty)
    df.loc[mask, 'Header 19'] = df.loc[mask, 'Header 6']
    df.loc[mask, 'Header 20'] = df.loc[mask, 'Header 9']

    # Convert the entire DataFrame to string before replacing empty strings
    df = df.astype(str)

    # Replace empty strings with 'nan' for columns 3 to 11
    df.loc[mask, 'Header 3':'Header 11'] = df.loc[mask, 'Header 3':'Header 11'].replace('', 'nan')

    # Write the DataFrame to a new CSV file
    df.to_csv(output_path, index=False)

    print("Conversion completed. Output file created.")

# Use 'script.py/input.csv' and 'script.py/output.csv' as file paths
convert_flat_file('script.py/input.csv', 'script.py/output.csv')
