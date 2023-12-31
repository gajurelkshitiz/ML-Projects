import glob
import pandas as pd

csv_files_pattern = 'Data/Real_data/Real_*.csv'
csv_files = glob.glob(csv_files_pattern)
dfs = []
for file in csv_files:
        df = pd.read_csv(file,skiprows=1,header=None)  # Specify header=None to ignore the existing header
        dfs.append(df)
combined_df = pd.concat(dfs, ignore_index=True)
combined_df.to_csv('Data/Cache_file.csv', index=False)

print(combined_df)

