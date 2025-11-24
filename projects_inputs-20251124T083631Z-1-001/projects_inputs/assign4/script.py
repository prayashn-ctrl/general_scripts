'''
Q4: Label with quantiles (Python)
Many times you want to get a sense of data by just plotting them in quantiles. 
The idea of quantiles is that equal number of datapoints will be there in each quantile. 
For example, median is a 50% quantile equally separating data points half and half. 
Your goal is to take a list of numbers from stdin and write a python code to label 
them which quantile they belong to. You would take an integer as argument from 
the user to know in how many quantiles you have to group. See an example below.

cat data/first_hundred_numbers.tsv | python group_in_quantiles.py 4 
75	q3	q3 (50.5, 75.25]
85	q4	q4 (75.25, 100.0]
44	q2	q2 (25.75, 50.5]
63	q3	q3 (50.5, 75.25]
27	q2	q2 (25.75, 50.5]
83	q4	q4 (75.25, 100.0]
90	q4	q4 (75.25, 100.0]
67	q3	q3 (50.5, 75.25]
77	q4	q4 (75.25, 100.0]
69	q3	q3 (50.5, 75.25]

The last column is the interval that defines those quantiles.

HINT: You can use qcut function from pandas library.

'''
# Usage = python script.py 4 < q4_data.tsv > output.tsv
# Usage = python script.py 4 < first_hundred_numbers.tsv > output2.tsv

from sys import stdin, stdout, argv
import pandas as pd

# read the incoming numbers into a small dataframe
vals = pd.read_csv(stdin, header=None, names=["num"])

# how many groups/quantiles to split into
k = int(argv[1])

# assign each number a quantile label (q1, q2, q3, ...)
vals["q_1"] = pd.qcut(vals["num"], q=k,
                      labels=[f"q{i+1}" for i in range(k)])

# second copy of the same label
vals["q_2"] = vals["q_1"]

# get the actual numeric interval for each number
vals["q_interval"] = pd.qcut(vals["num"], q=k)

# write final table (tab-separated, no header)
vals.to_csv(stdout, sep="\t", index=False, header=False)
