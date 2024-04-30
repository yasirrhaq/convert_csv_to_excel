import pandas as pd

# Path to your CSV file
csv_file_path = 'path_to_your_file.csv'
# Path output Excel file
excel_file_path = 'output_file.xlsx'

# Load CSV to data frame
df = pd.read_csv(csv_file_path)

# Write data frame to excel
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print("Conversion complete. The Excel file is saved as:", excel_file_path)
