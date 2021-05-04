import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read in csv data
images_df = pd.read_csv('../data/images_df.csv')

# plot and export bar chart of normalized distribution of character images between characters
images_df['char_name'].value_counts(normalize=True).plot(kind='bar')
plt.xticks(rotation=45)
plt.savefig('../data/char_distr_plot.jpg')
