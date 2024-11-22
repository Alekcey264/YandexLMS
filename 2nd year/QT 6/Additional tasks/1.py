import csv
import openpyxl

data = openpyxl.load_workbook(filename='data.xlsx', data_only=True)
sh_o = data.active
with open('output.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in sh_o.iter_rows(values_only=True):
        writer.writerow(row)