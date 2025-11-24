'''
Q2: Plotting a group of lines ( R + Linux Command)
A line plot requires X and Y values. But imagine, 
you have different set of Y values marked by categoires. 
You have to write a general purpose R code to plot multiple 
lines in the sample plot corresponding to different categories. 
You can find the data to plot here in the data directory (data/q2_data.tsv).
Your code should read from the standard input. 
You are likely going to use ggplot2, you will see the advantage of that here.

Your final code should run like the following

code :
$ cat data/q2_data.tsv | Rscript <your code.R> "different_clusters.png" "Relative from center [bp]" "Enrichment over Mean" "MNase fragment profile" 
'''


# Usage : python script.py < q2_data.tsv
import matplotlib.pyplot as plt 
import pandas as pd 
from sys import stdin

# Converting the tsv into dataframe structure with headers ["x-axis","y-axis","genes"]
all_data = pd.read_csv(stdin,sep="\t",header=None,names=["x-axis","y-axis","genes"])

# Using groupby so that each gene has its own line in graph 
for gene,data in all_data.groupby("genes") :
  plt.plot(data["x-axis"],data["y-axis"],label=gene)

# Lable box is shown
plt.legend()
# Saving in the output file 
plt.savefig("output.png")