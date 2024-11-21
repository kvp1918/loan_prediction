import kagglehub
import os
import pandas as pd

kagglehub.login()

# Download latest version
path = kagglehub.dataset_download("vikasukani/loan-eligible-dataset")

print("Path to dataset files:", path)

for filename in os.listdir(path):
    f = os.path.join(path, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        df = pd.read_csv(f)
        df.to_csv(f'./data/{filename}', index=False)