# Imports
import os
import pandas as pd

def convert_excel_to_csv(input_folder, output_folder):
    
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".xlsx"):
            excel_path = os.path.join(input_folder, filename)
            csv_path = os.path.join(output_folder, filename.replace(".xlsx", ".csv"))

            df = pd.read_excel(excel_path)

            df.to_csv(csv_path, index=False)