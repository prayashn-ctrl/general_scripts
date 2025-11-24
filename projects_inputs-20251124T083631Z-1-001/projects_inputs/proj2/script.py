# Usage : zcat query.bed.gz | python script.py reference.hist > output.tsv

import matplotlib.pyplot as plt
from sys import stdin, argv, stdout
import pandas as pd

# Load query BED as DataFrame
query_df = pd.read_csv(stdin, sep="\t", header=None, low_memory=False)

# Compute interval length
query_df["len"] = query_df[2] - query_df[1]

# Query length distribution
query_dist = query_df["len"].value_counts(normalize=True).sort_index()

# Plot query length distribution
plt.plot(
    query_dist.index,
    query_dist.values,
    label=f"query (n={len(query_df)})",
    color="purple",
    linewidth=0.5
)

# Load reference histogram
ref_df = pd.read_csv(argv[1], sep="\t", header=None, names=["len", "freq"])

# Plot reference histogram
plt.plot(
    ref_df["len"],
    ref_df["freq"],
    label="reference",
    color="green",
    linewidth=0.5
)

# Calculate how many rows to sample for each length
ref_df["count"] = ((ref_df["freq"] * len(query_df)) / 3).round()

# Collect sampled subsets
sampled = []

for _, row in ref_df.iterrows():
    length = row["len"]
    count = int(row["count"])

    # Subset with matching length
    subset = query_df[query_df["len"] == length]

    # Only sample if possible
    if count > 0 and len(subset) > 0:
        n = min(count, len(subset))
        sampled.append(subset.sample(n=n, random_state=1))

# Combine all sampled results
rescaled_df = pd.concat(sampled)

# Output rescaled dataset (TSV)
rescaled_df.to_csv(stdout, sep="\t", header=False, index=False)

# Rescaled distribution
rescaled_dist = rescaled_df["len"].value_counts(normalize=True)

# Plot rescaled distribution
plt.scatter(
    rescaled_dist.index,
    rescaled_dist.values,
    label=f"rep (n={len(rescaled_df)})",
    color="skyblue",
    marker="*",
    s=15
)

# Finalize plot
plt.legend()
plt.savefig("output.png")

