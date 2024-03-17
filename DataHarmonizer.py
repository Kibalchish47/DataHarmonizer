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