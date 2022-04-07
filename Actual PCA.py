#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 17:58:30 2021

@author: sarahcronin
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
#import plotly to plot PCA
#import matplotlib to plot histograms
import matplotlib.pyplot as plt

#import thinsection data from excel 
dFthinSectionData = pd.read_excel(r'C:\Users\therobe7\OneDrive\SRC_and_Research\MountJoy\TestCorrect Timpoweap Data sheet.xlsx',\
                                  sheet_name = 'AllData');
dFthinSectionData.set_index('Sample', inplace=True);
print(dFthinSectionData)
#Normalize the data
#scalerData = StandardScaler(dFthinSectionData);
pca = PCA(.70)
pca.fit(dFthinSectionData);
pThinSectionData = pca.transform(dFthinSectionData);
print(pca.n_components_)
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Component PCA', fontsize = 20)
tPCA = pca.components_
#Plot the 2 PCA
ax.scatter(pThinSectionData[0:8,0],pThinSectionData[0:8,1], c="blue", marker="o") 
ax.scatter(pThinSectionData[9:37:,0],pThinSectionData[9:37,1], c="red", marker="x")
plt.show()
