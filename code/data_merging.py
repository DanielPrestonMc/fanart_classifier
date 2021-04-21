import numpy as np
import pandas as pd
import os

files = os.listdir('../data/')

df = pd.DataFrame()

for file in files:
    df.concat(pd.read_csv(f'../data/{files}'))

print(df)
