#Used for reading and writing in excel(xlsx) files.
from openpyxl import load_workbook

# Load an existing Excel workbook
wb = load_workbook('example.xlsx')

# Select a specific sheet
sheet = wb.active  # or wb['SheetName'] to select a specific sheet

# Read a specific cell value (e.g., cell A1)
cell_value = sheet['A1'].value
print(f'Value in A1: {cell_value}')

# Loop through rows and columns to read data
for row in sheet.iter_rows(min_row=1, max_row=5, min_col=1, max_col=3):
    for cell in row:
        print(cell.value, end=' ')
    print()  # New line after each row
