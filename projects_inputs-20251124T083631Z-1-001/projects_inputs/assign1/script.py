'''
Q1: Selecting lines from stdin (Python Code + Linux Command)
Often, you would be interested in selecting lines from a file with patterns 
exactly matching your interest. The pattern, however, can either be i)
in a column somewhere in the file, ii) combination of columns or something more. 
You have to write a general code to select those lines. See the example below:
A query (to select lines) file may look like this (see data/to_select.tsv).

$ head -5 data/to_select.tsv
ENSG00000180353.10
ENSG00000180596.7
ENSG00000266379.6
ENSG00000262561.1
ENSG00000284999.1
And the big file from where you have to select may look like this (see data/q1_data.tsv.gz):
$ zcat data/q1_data.tsv.gz | awk 'NR==1||/ENSG/'  | head 

transcript_id(s)	gene_id	length	effective_length	expected_count	TPM	FPKM	posterior_mean_count	posterior_standard_deviation_of_count	pme_TPM	pme_FPKM	TPM_ci_lower_bound	TPM_ci_upper_bound	TPM_coefficient_of_quartile_variation	FPKM_ci_lower_bound	FPKM_ci_upper_bound	FPKM_coefficient_of_quartile_variation
ENST00000373020.8,ENST00000494424.1,ENST00000496771.5,ENST00000612152.4,ENST00000614008.4	ENSG00000000003.14	1224.31	1125.31	4.00	0.09	0.12	4.00	0.00	0.20	0.27	0.0683885	0.344228	0.25131	0.0955142	0.48334	0.251366
ENST00000373031.4,ENST00000485971.1	ENSG00000000005.5	940.50	841.50	0.00	0.00	0.00	0.00	0.00	0.08	0.11	0.00120747	0.1895	0.502341	0.00129288	0.26619	0.502379
ENST00000371582.8,ENST00000371584.8,ENST00000371588.9,ENST00000413082.1,ENST00000466152.5,ENST00000494752.1	ENSG00000000419.12	1077.43	978.43	803.00	20.76	28.51	803.00	0.00	20.46	28.76	19.0651	21.8942	0.0239603	26.8076	30.787	0.0239687
ENST00000367770.5,ENST00000367771.10,ENST00000367772.8,ENST00000423670.1,ENST00000470238.1	ENSG00000000457.13	3522.22	3423.22	564.00	4.17	5.72	564.00	0.00	4.14	5.82	3.70931	4.55996	0.0355908	5.23182	6.42815	0.0356293
ENST00000286031.10,ENST00000359326.8,ENST00000413811.3,ENST00000459772.5,ENST00000466580.6,ENST00000472795.5,ENST00000481744.5,ENST00000496973.5,ENST00000498289.5	ENSG00000000460.16	2091.02	1992.02	794.00	10.08	13.85	794.00	0.00	9.88	13.88	8.79838	10.9956	0.0383398	12.3933	15.4827	0.0383309
ENST00000374003.7,ENST00000374004.5,ENST00000374005.7,ENST00000399173.5,ENST00000457296.5,ENST00000468038.1,ENST00000475472.5	ENSG00000000938.12	1984.18	1885.18	2435.00	32.68	44.87	2435.00	0.00	31.95	44.91	30.3246	33.631	0.0179456	42.6014	47.2517	0.0179483
ENST00000359637.2,ENST00000367429.8,ENST00000466229.5,ENST00000470918.1,ENST00000496761.1,ENST00000630130.2	ENSG00000000971.15	2375.79	2276.79	16.43	0.18	0.25	16.32	0.47	0.31	0.43	0.121935	0.522164	0.234572	0.171868	0.734625	0.234607
ENST00000002165.10,ENST00000367585.1,ENST00000451668.1	ENSG00000001036.13	1869.59	1770.59	905.00	12.93	17.76	905.00	0.00	12.69	17.84	11.4186	14.0078	0.0349594	16.0494	19.688	0.0349339
ENST00000229416.10,ENST00000504353.1,ENST00000504525.1,ENST00000505197.1,ENST00000505294.5,ENST00000509541.5,ENST00000510837.5,ENST00000513939.6,ENST00000514004.5,ENST00000514373.3,ENST00000514933.2,ENST00000515580.1,ENST00000616923.5,ENST00000643939.1,ENST00000650454.1	ENSG00000001084.12	2290.61	2191.61	690.00	7.97	10.94	690.00	0.00	8.53	11.99	6.82069	10.1848	0.0676588	9.58672	14.3148	0.067699

2nd column contains your patterns of interest. 
But, your final run (code + linux command) should be in a way that code should not be sensitive to the column position of your pattern in the file. 
Of course, you are free to use stdin and other linux commands to mend it to your way. 
You have to think how to keep your code general so that when you are working in different scenario, you don't have to make changes in the code.
As instructed above, your thoughts explained on your GitHub repo will earn 0.5 marks and your coding 1.5.
'''

# Usage : zcat q1_data.tsv.gz | python script.py to_select.tsv 2 > output.tsv
from sys import stdin, stdout, argv

# Which column to check (1-based input → convert to 0-based index)
col_num = int(argv[2]) - 1

# Read the list of values to match from the query file
with open(argv[1]) as query_file:
    match_set = {line.strip() for line in query_file}

# Go through each line of the big input file
for line in stdin:

    # Split the line into columns
    parts = line.strip().split("\t")

    # If the value in the chosen column is in the match list
    if parts[col_num] in match_set:

        # Print the original line
        stdout.write(line)

