import pickle
#import networkx as nx
import numpy as np
from matplotlib import pyplot as plt


def recommend_product(item_list):
    rules = pickle.load(open('rules.pkl', 'rb'))
    rules['antecedent'] = rules['antecedents'].apply(lambda antecedent: list(antecedent))
    rules['consequent'] = rules['consequents'].apply(lambda consequent: list(consequent))
    rules['rule'] = rules.index
    #print(rules['antecedent'])

    cons_list = []
    for i in range(1, len(rules)):
        check = all(item in (rules['antecedent'][i]) for item in item_list)
        if check is True:
            c_list = set(list(rules['consequents'])[i])
            cons_list.append(c_list)
    print(cons_list)
    output = []
    for x in cons_list:
        if x not in output:
            output.append(x)
    print(output)
    return output