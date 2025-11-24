# Usage : tar -xzf ../tcga_data.tar.gz     
# Usage : python script.py unzip < gdc_sample_sheet.tsv

from sys import stdin,argv
import pandas as pd
import os

# first argument is the directory containing the extracted data folders
base_dir = argv[1]

# storage for sample IDs and TPM values
sample_ids = []
nkx2_tpm = []

# iterate through each sample directory
for sample_folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, sample_folder)

    # look inside each folder for the gene count file
    for item in os.listdir(folder_path):
        if item.endswith(".tsv"):
            file_path = os.path.join(folder_path, item)

            # parse file and search for target gene
            with open(file_path) as handle:
                for ln in handle:
                    fields = ln.rstrip("\n").split("\t")

                    # NKX2-1 appears as one field in the row → pick TPM column
                    if "NKX2-1" in fields:
                        nkx2_tpm.append(fields[6])
                        sample_ids.append(sample_folder)
                        break   # no need to inspect more lines in this file

# convert to a dataframe
df_expr = pd.DataFrame({"id": sample_ids, "tpm": nkx2_tpm})

# ---------------------------------------
# read tissue condition from sample sheet
# ---------------------------------------

sheet_ids = []
sheet_cond = []

for row in stdin:
    parts = row.strip().split("\t")

    # check sample category
    if "Solid Tissue Normal" in row:
        sheet_ids.append(parts[0])
        sheet_cond.append("Solid Tissue Normal")

    elif "Primary Tumor" in row:
        sheet_ids.append(parts[0])
        sheet_cond.append("Primary Tumor")

df_meta = pd.DataFrame({"id": sheet_ids, "cond": sheet_cond})

# combine metadata with expression information
final_df = pd.merge(df_expr, df_meta, on="id")

# save output table exactly as required
final_df.to_csv("output.tsv", sep="\t", index=False, header=False)