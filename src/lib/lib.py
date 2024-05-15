import csv
from datetime import datetime

def display(acc):
    for i in range(len(acc)):
        print(acc[i])

def read_in(acc, filename, h_date, h_name, h_amount):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date = create_dates(row[h_date]) # look down
            # date = row["Posting Date"]
            name = row[h_name]
            amount = create_numbers(row[h_amount])
            acc.append({
                h_date: date,
                h_name: name,
                h_amount: amount,
            })

def create_dates(date):
    new_date = datetime.strptime(date, "%m/%d/%Y")
    return new_date

def create_numbers(num):
    return float(num)

def filter_unwanted(acc, names, desc):
    for i in range(len(acc) - 1, -1, -1):
        if any(acc[i][desc].startswith(name) for name in names):
            acc.pop(i)

def filter_month(acc, month, date):
    for i in range(len(acc) - 1, -1, -1):
        if acc[i][date].month != month:
            acc.pop(i)

def write_out(acc, filename):
    keys = acc[0].keys() if acc else []
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(acc)

def read_filter(filename):
    with open(filename, "r") as file:
        unwanted_txn = [line.strip() for line in file]
    return unwanted_txn
