import numpy as np
import pandas as pd

my_dict = {
    'name':'Daniel',
    'age':[36, 38, 32],
    'sign':['Pisces','Scorpio','Taurus'],
    'occupation':['Student','Housing','Server']
}

my_dict['age'].append(45)
my_dict['sign'].append('Cat')
my_dict['occupation'].append('Dog')

my_df = pd.DataFrame(my_dict)

print(my_df)
