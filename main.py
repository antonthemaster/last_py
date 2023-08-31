import pandas as pd
import random


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


unique_values = data['whoAmI'].unique()
one_hot_dict = {value: [] for value in unique_values}


for value in unique_values:
    one_hot_dict[value] = [1 if v == value else 0 for v in data['whoAmI']]


one_hot_df = pd.DataFrame(one_hot_dict)
result_df = pd.concat([data, one_hot_df], axis=1)

print(result_df.head())