# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:53:32 2021

@author: KHUSHI
"""

import pandas as pd
import numpy as np
eps = np.finfo(float).eps
from numpy import log2 as log

df = pd.read_csv('bank.csv')
def find_entropy(df):
    Class = df.keys()[-1]  
    entropy = 0
    values = df[Class].unique()
    for value in values:
        fraction = df[Class].value_counts()[value] / len(df[Class])
        entropy += -fraction * np.log2(fraction)
    return entropy


def find_entropy_attribute(df, attribute):
    Class = df.keys()[-1]  
    target_variables = df[Class].unique()  #  all 'Yes' and 'No'
    variables = df[attribute].unique()  # different features in that attribute 
    entropy2 = 0
    for variable in variables:
        entropy = 0
        for target_variable in target_variables:
            num = len(df[attribute][df[attribute] == variable][df[Class] == target_variable])
            den = len(df[attribute][df[attribute] == variable])
            fraction = num / (den + eps)
            entropy += -fraction * log(fraction + eps)
        fraction2 = den / len(df)
        entropy2 += -fraction2 * entropy
    return abs(entropy2)


def best_att(df):
    IG = []
    for key in df.keys()[:-1]:
        #       Entropy_att.append(find_entropy_attribute(df,key))
        IG.append(find_entropy(df) - find_entropy_attribute(df, key))
        #print("reached here winner")
    return df.keys()[:-1][np.argmax(IG)]


def get_subframe(df, node, value):
    return df[df[node] == value].reset_index(drop=True)


def buildTree(df, tree=None):
    # maximum information gain
    node = best_att(df)
    print(node)
    # Get distinct value of that attribute e.g Salary is node and Low,Med and High are values
    attValue = np.unique(df[node])
    # Create an empty dictionary for tree
    if tree is None:
        tree = {}
        tree[node] = {}

    for value in attValue:
        subframe = get_subframe(df, node, value)
        #print(subframe);
        clValue, counts = np.unique(subframe['loan'], return_counts=True)

        if len(counts) == 1:  # Checking purity of subset
            tree[node][value] = clValue[0]   
        else:
           #print("----------new call--------------")
            tree[node][value] = buildTree(subframe)  # Calling the function recursively
    return tree


t=buildTree(df)
import pprint
pprint.pprint(t)
