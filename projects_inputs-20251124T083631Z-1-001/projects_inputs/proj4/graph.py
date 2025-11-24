# Usage : python graph.py < output.tsv

import matplotlib.pyplot as plt
from sys import stdin
import math
from scipy import stats

# accumulate log2(TPM + 1) values for tumor and normal samples
tum, nor = [], []

# read table from stdin, one record per line
for raw in stdin:
    parts = raw.strip().split("\t")
    if len(parts) < 3:
        # skip malformed rows
        continue

    # compute y value = log2(TPM + 1)
    value = float(parts[1])
    log2_val = math.log2(value + 1)

    # distribute into the appropriate list
    if parts[2] == "Solid Tissue Normal":
        nor.append(log2_val)
    else:
        tum.append(log2_val)

# compute two-sample t-test (independent samples)
t, p = stats.ttest_ind(tum, nor)

# create a notch boxplot: normals first, tumors second
plt.boxplot([nor, tum],
           tick_labels=[f"Solid Tissue Normal (n = {len(nor)})",
                    f"Primary Tumor (n = {len(tum)})"],
            notch=True)

# annotate axes and title (show p-value in scientific notation)
plt.ylabel("log2(TPM + 1)")
plt.title(f"Lung Adenocarcinoma (p = {p:.1e})")

# tidy layout and save the figure
plt.tight_layout()
plt.savefig("output.png", dpi=300)