# Usage : zcat shuf.a.bed.gz shuf.b.bed.gz > combined.bed
# Usage : cat combined.bed | python script.py standard_selection.tsv > output.tsv
from sys import stdin, stdout, argv
import pandas as pd 

# Storing the input in a dataframe
all_data = pd.read_csv(stdin, sep="\t", header=None, low_memory=False)

# Storing the selsction datas in a list
with open(argv[1]) as f1:
    chm_lt = [line.strip() for line in f1]

# Defining order in first column
all_data[0] = pd.Categorical(all_data[0], categories=chm_lt, ordered=True)

# Sorting each column
all_data = all_data.sort_values(by=[0, 1, 2],kind="mergesort")

# Converting a dataframe to tsv file 
all_data.to_csv(stdout, sep="\t", header=False, index=False)
