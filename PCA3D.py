# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:17:18 2022

@author: therobe7
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
#import plotly to plot PCA
#import matplotlib to plot histograms
import matplotlib.pyplot as plt
#import statsmodel for Kolmogorov-Smirnov test to determine if the samples came from the same distribution
from scipy.stats import ks_2samp, kurtosis, skew

#set the figure resolution much higher:
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 500

#import thinsection data from excel 
dFthinSectionData = pd.read_excel(r'C:\Users\duckm\OneDrive\SRC_and_Research\MountJoy\TestCorrect Timpoweap Data sheet.xlsx',\
                                  sheet_name = 'AllData')
dFthinSectionData.set_index('Sample', inplace=True);

mLabels = pd.read_excel(r'C:\Users\duckm\OneDrive\SRC_and_Research\MountJoy\TestCorrect Timpoweap Data sheet.xlsx',\
                                  sheet_name = 'Labels')
    
#print(dFthinSectionData)

#Normalize the data
#scalerData = StandardScaler(dFthinSectionData)
#scalerData = StandardScaler(dFthinSectionData.loc('Irregular fenestra':'Seafloor micrite'))

#Perform PCA
dVar = .70
pca = PCA(dVar)
pca.fit(dFthinSectionData)
pThinSectionData = pca.transform(dFthinSectionData)
print('Number of components:', pca.n_components_)
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1, projection='3d') 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_zlabel('Principal Component 3', fontsize = 15)
ax.set_title('3 Component PCA', fontsize = 20)
#tPCA = pca.components_


## TODO 
ax.scatter(pThinSectionData[:,0],pThinSectionData[:,1],pThinSectionData[:,2], c=mLabels['Color'], marker="o")
#ax.scatter(pThinSectionData[0:8,0],pThinSectionData[0:8,1],pThinSectionData[0:8,2], c="blue", marker="o") # plot the point (2,3,4) on the figure
#ax.scatter(pThinSectionData[9:28:,0],pThinSectionData[9:28,1],pThinSectionData[9:28,2],c="red", marker="x")
plt.show()



