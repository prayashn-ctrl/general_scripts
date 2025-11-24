# Usage : cat output.tsv | python graph.py 

import sys
import pandas as pd
import matplotlib.pyplot as plt

# read tab-separated data from stdin and name columns differently to avoid looking identical
data = pd.read_csv(sys.stdin, sep="\t", header=None, names=["dx", "frag_len", "count"])

# guard against empty input
if data.empty:
    raise SystemExit("No data supplied on stdin. Expected tab-separated x, y, i columns.")

# prepare a figure with two vertical panels (top panel is smaller than bottom)
figure, axes = plt.subplots(nrows=2, ncols=1, gridspec_kw={"height_ratios": [1, 3]})

# scatter on top: color by 'count', tiny markers and partial transparency
top_scatter = axes[0].scatter(data["dx"], data["frag_len"], c=data["count"],
                              cmap="BuPu", s=1, alpha=0.7)
axes[0].set_xlim(-500, 500)
axes[0].set_ylim(0, 200)
figure.colorbar(top_scatter, ax=axes[0])

# scatter on bottom: same style but narrower x-range
bottom_scatter = axes[1].scatter(data["dx"], data["frag_len"], c=data["count"],
                                 cmap="BuPu", s=1, alpha=0.7)
axes[1].set_xlim(-200, 200)
axes[1].set_ylim(0, 200)
figure.colorbar(bottom_scatter, ax=axes[1], label="Fragment centre count")

# shared axis labels using figure-level text for consistent placement
figure.text(0.5, 0.02, "Distance from motif center (bp)", ha="center", va="bottom")
figure.text(0.02, 0.5, "cfDNA fragment length (bp)", va="center", ha="left", rotation="vertical")

# save with high resolution and tight bounding box (same appearance as original)
plt.savefig("output.png", dpi=600, bbox_inches="tight")
