
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

def group_by(table, header, group_by_col_name):
    col = get_column(table, header, group_by_col_name)
    col_index = header.index(group_by_col_name)

    # get a list of unique values for the column
    group_names = sorted(list(set(col))) # 75, 76, 77
    group_subtables = [[] for _ in group_names] # [[], [], []]

    # walk through each row and assign it to the appropriate
    # subtable based on its group by value (model year)
    for row in table:
        group_value = row[col_index]
        # which group_subtable??
        group_index = group_names.index(group_value)
        group_subtables[group_index].append(row.copy()) # shallow copy

    return group_names, group_subtables

def compute_equal_width_cutoffs(values, num_bins):
    # first compute the range of the values 
    values_range = max(values) - min(values)
    bin_width = values_range / num_bins 
    # N + 1 cutoffs
    # bin_width is probably a float
    # if your application allows, use ints
    # we will use floats, but with numpy
    cutoffs = list(np.arange(min(values), max(values), bin_width))
    cutoffs.append(max(values))
    # optionally round
    cutoffs = [round(cutoff, 2) for cutoff in cutoffs]
    return cutoffs 

def compute_bin_frequencies(values, cutoffs):
    freqs = [0 for _ in range(len(cutoffs) - 1)]

    for val in values:
        if val == max(values):
            freqs[-1] += 1
        else:
            for i in range(len(cutoffs) - 1):
                if cutoffs[i] <= val < cutoffs[i + 1]:
                    freqs[i] += 1

    return freqs

def compute_slope_intercept(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y) 
    m = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))]) \
        / sum([(x[i] - mean_x) ** 2 for i in range(len(x))])
    # y = mx + b => y - mx
    b = mean_y - m * mean_x
    return m, b 

def dummy_function1():
    pass

def dummy_function2():
    pass