import openpyxl as xl

# Loads excel workbook
wb = xl.load_workbook('transactions.xlsx')
# Gets sheet 
sheet = wb['Sheet1']
# Gets cell
cell = sheet['a1']
print(sheet.max_row)

for row in range(2, sheet.max_row + 1):
    # gets what is in each cell in the row
    cell = sheet.cell(row, 3)
    print(cell.value)

