# saving character names and associated image path information to dataframe
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

from PIL import Image

# create empty dataframe
images_df = pd.DataFrame(columns=['char_name','img_path'])

# create list of all character name strings by folder names
name_list = [name for name in os.listdir('../assets/')]

# iterate through each character folder
for name in name_list:
    path = os.listdir(f'../assets/{name}/')

    # iterate through each image in character folder, adding character name and image path to dataframe
    for image in path:

        images_df = images_df.append({'char_name': name,
                                    'img_path': f'../assets/{name}/{image}'
                                   }, ignore_index=True)

# saving dataframe to csv file
images_df.to_csv('../data/images_df.csv', index=False)

print(images_df.tail())
