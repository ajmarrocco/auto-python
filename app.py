import openpyxl as xl

# Loads excel workbook
wb = xl.load_workbook('transactions.xlsx')
# Gets sheet 
sheet = wb['Sheet1']
# Gets cell
cell = sheet['a1']
print(cell.value)


