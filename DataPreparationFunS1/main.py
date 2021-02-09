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

def main():
    header = ["CarName", "ModelYear", "MSRP"]
    msrp_table = [["ford pinto", 75, 2769],
                ["toyota corolla", 75, 2711],
                ["ford pinto", 76, 3025],
                ["toyota corolla", 77, 2789],
                ["honda accord", 76, 3999]]
    msrps = get_column(msrp_table, header, "MSRP")
    print(msrps)

    # warm up
    modelyear_values, modelyear_counts = get_frequencies(msrp_table, header, "ModelYear")
    print(modelyear_values)
    print(modelyear_counts)

    # more on attributes
    # 1. what is the type of the attribute?
    # how is it stored?
    # e.g. int, float, str, bool, etc. 
    # 2. what is the semantic value of the attribute (and its values)?
    # what do the values mean/represent?
    # domain knowledge!!
    # 3. what scale was the attribute measured on?
    # categorical vs continuous
    # nominal: categorical with out an inherent ordering
    # e.g. names, colors, ...
    # ordinal: categorical with ordering
    # e.g. t-shirt sizes (S, M, L, XL, etc...), letter grades (A, A-, B+, ...)
    # ratio-scaled: continuous where 0 means an "absence"
    # e.g 0 lbs in weight is an absence of weight
    # e.g. 0 degrees in K is an absence of temperature
    # interval-scaled: continuous without inherent absence value
    # e.g. 0 degrees F

    # noisy vs invalid data
    # noisy: valid on the scale, but recorded incorrectly
    # e.g. 18 years old but 81 is entered for age
    # invalid: not valid on the scale
    # e.g. "bob" for an age value

    # missing values
    # two main ways to deal with missing values
    # 1. discard them
    # really only do this when the dataset is large and missing values
    # are small (never throw away data)
    # 2. fill them
    # categorical attribute: majority voting system (e.g. most frequent value)
    # continuous attribute: central tendency measure (e.g. average, median, et.c)
    # more on this later: intelligently... like maybe do some groups, or use kNN...

    # summary stats
    # mid value (mid range): (min + max) / 2
    # min, max
    msrp_min, msrp_max = get_min_max(msrps)
    print("min:", msrp_min, "max:", msrp_max)
    # arithmetic mean
    msrp_mean = sum(msrps) / len(msrps)
    print("mean:", msrp_mean)
    # means are subject to extreme values (outliers)
    # someties we prefer the median (the middle value in the sorted list)
    # mode: the most frequently occuring

    # data dispersion
    # variance measures the spread of the data
    # low variance: data is close to the mean
    # standard deviation: square root of variance
    # compute variance and stdev and compare with numpy
    # variance: average of the squared mean deviations
    squared_mean_deviations = [(x - msrp_mean) ** 2 for x in msrps] # list comprehension
    msrp_variance = sum(squared_mean_deviations) / len(squared_mean_deviations)
    msrp_stdev = math.sqrt(msrp_variance)
    print("stdev:", msrp_stdev, np.std(msrps))

    # for normally distributed data (bell shaped curve)
    # empirical rule
    # 68% of the data is within mean +/- 1 stdev
    # 95% of the data is within mean +/- 2 stdev
    # 99.7% of the data is within mean +/- 3 stdev

    # talk about quantiles
    # quantiles are used to partition (sorted) data into
    # roughly equal sized groups
    # 2-quantiles: 2 groups; 1 cut-off point (median)
    # quartiles: 4 groups; 3 cut-offs
    # percentiles: 100 groups; 99 cut-offs 
    # more on percentiles later...


if __name__ == "__main__":
    main()