import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pickle as pickle
import seaborn as sns


data = pd.read_csv("../Data set/associationRule_dataset.csv", header= None)
data.columns = ["ID","Date","Items"]

data.drop('Date', inplace=True, axis=1)

data.drop(0, inplace=True, axis=0)

data1 = data.groupby('ID')['Items'].apply(','.join).reset_index()
pd.set_option('display.max_rows', data.shape[0] + 1)

transac = []
for i in range(0, len(data1)):
    transac.append([str(data1.values[i, j]) for j in range(0, 2) if str(data1.values[i, j]) != '0'])

itemArray = data['Items'].unique()

df = data.groupby('ID')['Items'].apply(','.join).reset_index()

for i in range(0, len(itemArray)):
    df.insert(len(df.columns), itemArray[i], "")
    for index, row in df.iterrows():
        df.at[index, itemArray[i]] = 1 if len(
            [1 for item in transac[index][1].split(",") if item in itemArray[i]]) > 0 else 0

df.drop('Items', inplace=True, axis=1)

frequent_itemsets = apriori(df.drop(['ID'], axis=1), min_support=0.0040, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)

pickle.dump(rules, open('rules.pkl', 'wb'))