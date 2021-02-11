
import math 
import numpy as np 

# warmup task
def get_column(table, header, col_name):
    col_index = header.index(col_name)
    col = []
    for row in table: 
        # ignore missing values ("NA")
        if row[col_index] != "NA":
            col.append(row[col_index])
    return col

def get_min_max(values):
    # you can return multiple values
    # via a tuple (immutable list that is often used for packing and unpacking
    # values)
    return min(values), max(values)

def get_frequencies(table, header, col_name):
    col = get_column(table, header, col_name)

    col.sort() # inplace
    values = []
    counts = []

    for value in col:
        if value not in values:
            # first time we have seen this value
            values.append(value)
            counts.append(1)
        else:
            # we have seen this value before 
            counts[-1] += 1 # ok because the list is sorted

    return values, counts

def dummy_function1():
    pass