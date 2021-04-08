import pandas as pd
import numpy as np
import requests
import json

# Reference: https://www.dataquest.io/blog/python-api-tutorial/

res = requests.get('https://api.census.gov/data/timeseries/pseo/earnings?get=LABEL_INSTITUTION,LABEL_INST_STATE,LABEL_INST_LEVEL,LABEL_GRAD_COHORT_YEARS,LABEL_DEGREE_LEVEL,Y1_GRADS_EARN,Y5_GRADS_EARN,Y10_GRADS_EARN&key=924eb23346ed8efcec05b6794a12c6be307df352')

data_list = res.json()
df = pd.DataFrame(data_list[1:], columns=data_list[0])
df.columns = df.columns.str.lower()

# df.to_csv('data/college_data.csv')
