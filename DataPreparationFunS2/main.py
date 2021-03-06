import math 
import numpy as np # for checking our std work

# warm up task
def get_column(table, header, col_name):
    col_index = header.index(col_name)
    col = []

    for row in table:
        if (row[col_index] != "NA"):
            col.append(row[col_index])
    return col 

def get_min_max(values):
    # return 2 values
    # multiple values are packed into a tuple
    # tuple: an immutable list
    return min(values), max(values)

# warm up 
def get_frequencies(table, header, col_name):
    col = get_column(table, header, col_name)
    col.sort() 

    values = []
    counts = []

    for value in col:
        if value not in values:
            # haven't seen this value before
            values.append(value)
            counts.append(1)
        else:
            # have seen this value before
            counts[-1] += 1 # ok because col is sorted

    return values, counts 

def main():
    header = ["CarName", "ModelYear", "MSRP"]
    msrp_table = [["ford pinto", 75, 2769],
              ["toyota corolla", 75, 2711],
              ["ford pinto", 76, 3025],
              ["toyota corolla", 77, 2789],
              ["ford mustang", 77, 3999],
              ["tesla", 74, 5000]]
    msrps = get_column(msrp_table, header, "MSRP")
    print(msrps)

    # warmup 
    modelyear_values, modelyear_counts = get_frequencies(msrp_table, header, "ModelYear")
    print(modelyear_values)
    print(modelyear_counts)
    # more on attributes
    # 1. what is the type of an attribute?
    # what is the most appropriate way to store the attribute
    # e.g. int, float, str, bool, etc...
    # 2. what is the semantic value/type of an attribute?
    # what do the values of the attribute mean/represent?
    # domain knowledge!!
    # 3. what is the scale the attribute is recorded on?
    # categorical or continuous
    # nominal: categorical scale without an inherent ordering
    # e.g. names, colors, etc.
    # ordinal: categorical with an ordering
    # e.g. t-shirt sizes (S, M, L, XL, ...), letter grades (A, A-, B+, ...)
    # ratio-scaled: continuous where 0 means "absence"
    # e.g. 0 lbs (absence of weight), 0 degrees K (absence of temperature)...
    # interval-scaled: continuous where 0 doesn't imply absence
    # e.g. 0 degrees F

    # noisy vs invalid values
    # noisy: valid on the scale, but recorded incorrectly
    # e.g. 18 year old recorded with an age of 81
    # invalid: not valid on the scale
    # e.g. "bob" for an age

    # missing values
    # usually denoted "?" "NA" "" NaN
    # dealing with missing values
    # 1. discard values
    # works well when you have a large dataset and the quantity of missing values are small
    # don't want to throw data away
    # 2. fill the values
    # categorical: majority voting system (e.g. the most frequent label)
    # continuous: central tendency measures (e.g. median, mean, etc.)
    # for future conversations... fill more intelligently...
    # with the average of a subgroup or with kNN, etc...

    # summary stats 
    # mid range (mid value): (min + max) / 2
    # min, max
    msrp_min, msrp_max = get_min_max(msrps) 
    print("min:", msrp_min, "max:", msrp_max)
    # central tendency measures
    # arithmetic mean
    msrp_mean = sum(msrps) / len(msrps) 
    # mean is subject to extreme values (outliers)
    # sometimes prefer the median instead (middle value in a sorted list)
    # mode: is the most frequently occuring value

    # data dispersion
    # variance: measures the spread of the data
    # low variance, data is close to the mean
    # average of the squared mean deviations
    squared_mean_deviations = [(x - msrp_mean) ** 2 for x in msrps] # list comprehension
    msrp_variance = sum(squared_mean_deviations) / len(squared_mean_deviations)
    # standard deviation: square root of variance
    msrp_stdev = math.sqrt(msrp_variance)
    print("msrp stdev:", msrp_stdev, np.std(msrps))

    # for normally distributed data (bell shaped curve)
    # empirical rule
    # 68% of data values are within mean +/- 1 stdev
    # 95% of data values are within mean +/- 2 stdev
    # 99.7% of data values are within mean +/- 3 stdev

    # quantiles
    # are used to partition (sorted) data into roughly
    # equal sized groups
    # 2-quantiles: 2 groups; 1 cut off point (median)
    # quartiles: 4 groups; 3 cut off points
    # percentiles: 100 groups; 99 cut off points
    # more on this later


if __name__ == "__main__":
    main()