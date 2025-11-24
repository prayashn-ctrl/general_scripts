'''
Q3: Merge multiple files 
Often, you will run into merging multiple files by any 
given column that contains the keys of your interest. 
Write a general R script which will take a file with the 
list of file names needs to be merged. The output should be in stdout. 
It can simply be then directed to the desired file as output.
Your code will take data/list_q3.tsv as input, and produce inner join 
(meaning that the first column values that is common between both of the files).

$ cat data/list_q3.tsv 
data/q3_first.tsv
data/q3_second.tsv

Your code should run like the following:
Rscript join_list_of_files.py data/list_q3.tsv  > data/join_output.tsv

The output in the stdout should look like the following:

81d92351-c619-4585-9281-de33eaaabba4	TCGA-38-7271-01A	Primary Tumor	13.6971
2e5071ce-d8cf-46e5-9cc0-91353f0d643c	TCGA-55-7914-01A	Primary Tumor	24.8212
d3f1b81f-37ce-47b6-b98d-8530076007c7	TCGA-95-7043-01A	Primary Tumor	15.7251
c568fdc8-6942-44ff-a9d9-3f7a03fdc62a	TCGA-73-4658-01A	Primary Tumor	61.6106
dd6ec250-8d4d-4129-9664-7451c1760f4b	TCGA-86-8076-01A	Primary Tumor	28.685
9711a58c-08fc-428f-93a1-3d3db7df213e	TCGA-55-7726-01A	Primary Tumor	135.6884
3c9960fd-92f3-4bab-9771-933c95edc37f	TCGA-44-6147-01A	Primary Tumor	15.2054
b080156e-0711-42f5-83c7-a34de25cbba9	TCGA-50-5932-01A	Primary Tumor	14.6362
c3e2e99a-537a-4263-a835-fef5ed2c3588	TCGA-44-2661-01A	Primary Tumor	18.2345
cb59cd67-2756-45e1-80c7-67ad6d6823d4	TCGA-86-7954-01A	Primary Tumor	36.8657


NOTE: you would need tidyverse library for joining. Please install that. See the function called reduce.

'''
# Usage : cat q3_first.tsv | python script.py q3_second.tsv > output.tsv
from sys import stdin, stdout, argv

# Load the second file (given as argument) into a lookup table
with open(argv[1]) as f2:
    join_map = {}
    for line in f2:
        pieces = line.rstrip("\n").split("\t", maxsplit=1)
        join_map[pieces[0]] = pieces[1]

# Read the first file from stdin and match rows based on the first column
for line in stdin:
    parts = line.rstrip("\n").split("\t", maxsplit=1)
    key = parts[0]

    # inner join: only keep keys present in both files
    if key in join_map:
        merged_row = parts[0] + "\t" + parts[1] + "\t" + join_map[key]
        stdout.write(merged_row + "\n")
