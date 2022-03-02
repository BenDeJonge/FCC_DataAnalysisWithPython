# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:40:36 2021

@author: BenDJ

Plotting a histogram of the weights and heights stored in 
'medical-examination.csv' to check how realistic the automated slicing based
on the 2.5%-97.5% quantiles is.
"""

import pandas as pd
import matplotlib.pyplot as plt

class Histogram:
    def __init__(self, title, xlabel, ylabel, data, bins):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.data = data
        self.bins = bins
     
    def setup_hist(self):
        fig = plt.figure()
        ax = fig.add_axes( [0,0,1,1] )
        ax.set_title(self.title)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        counts, edges, plot = ax.hist(self.data, bins = self.bins)
        
        self.countDict = {f'{self.bins[i]} - {self.bins[i+1]}' : counts[i] 
                      for i in range(len(self.bins) - 1)}
        
df = pd.read_csv('medical_examination.csv')

histHeight = Histogram( 'Height', 'Height', 'Counts',
                        df.height, bins=list(range(130, 201, 5)) )
histWeight = Histogram( 'Weight', 'Weight', 'Counts',
                        df.weight, bins=list(range(10, 211, 5)) )
histHeight.setup_hist()
print(histHeight.countDict)
print(df.height.quantile(0.025))
print(df.height.quantile(0.975))
print()
histWeight.setup_hist()
print(histWeight.countDict)
print(df.weight.quantile(0.025))
print(df.weight.quantile(0.975))