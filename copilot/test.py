# write a function that parses a .csv and returns the number of asterisk characters in the file

import csv

def count_asterisks(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            count += row.count('*')
        return count


