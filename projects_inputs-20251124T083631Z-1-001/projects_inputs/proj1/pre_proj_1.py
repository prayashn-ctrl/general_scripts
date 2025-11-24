# Usage : python selection_script.py > standard_selection.tsv

from sys import stdout

for i in range(1,23) :
  print(f"chr{i}")
stdout.write(f"chrX\nchrY")