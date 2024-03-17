# Imports
import os
import pandas as pd

def convert_excel_to_csv(input_folder, output_folder):
    """
    Converts Excel files in the input folder to CSV files in the output folder.

    Args:
        input_folder (str): Path to the input folder containing Excel files.
        output_folder (str): Path to the output folder where CSV files will be saved.
    """
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through Excel files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".xlsx"):
            excel_path = os.path.join(input_folder, filename)
            csv_path = os.path.join(output_folder, filename.replace(".xlsx", ".csv"))

            # Read Excel file
            df = pd.read_excel(excel_path)

            # Replace empty values with zeros
            df.fillna(0, inplace=True)

            # Save as CSV
            df.to_csv(csv_path, index=False)

def identify_common_columns(csv_files):
    """
    Identifies common columns across multiple CSV files.

    Args:
        csv_files (list): List of paths to CSV files.

    Returns:
        set: Set of common column names.
    """
    # Read the first CSV file to get column names
    first_csv = pd.read_csv(csv_files[0])
    common_columns = set(first_csv.columns)

    # Compare with other CSV files
    for csv_file in csv_files[1:]:
        df = pd.read_csv(csv_file)
        common_columns &= set(df.columns)

    return common_columns
       
if __name__ == "__main__":
    input_folder = "spreadsheets_input"  # Replace with actual input folder path
    output_folder = "spreadsheets_output"  # Replace with actual output folder path

    # Step 1: Convert Excel to CSV
    convert_excel_to_csv(input_folder, output_folder)

    # Step 2: Identify common columns

    print("Processing completed. CSV files saved in the output folder.")