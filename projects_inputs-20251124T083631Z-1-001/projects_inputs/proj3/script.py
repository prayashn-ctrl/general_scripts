# Bash:  zcat mapped.bed.gz | python script.py > output.tsv

from sys import stdin, stdout
from collections import defaultdict

# Nested dictionary: offsets[x_value][y_value] = count
offsets = defaultdict(lambda: defaultdict(int))

# Looping inside the input file
for ln in stdin:
  # Looping inside the input file
    cols = ln.rstrip("\n").split("\t")
    #protect the code from crashes when a line in the BED file does not contain at least 12 columns.
    if len(cols) < 12:
        continue

    # midpoint of the original (undigested) region
    mid_original = (int(cols[2]) + int(cols[3])) * 0.5

    # midpoint of the digested (protected) region
    mid_frag = (int(cols[8]) + int(cols[9])) * 0.5

    # horizontal shift (x-coordinate)
    dx = mid_frag - mid_original

    # fragment length (y-coordinate)
    frag_len = int(cols[11])

    # accumulate
    offsets[dx][frag_len] += 1

# Output all records
for dx_val, subdict in offsets.items():
    for length_val, count in subdict.items():
        stdout.write(f"{dx_val}\t{length_val}\t{count}\n")
