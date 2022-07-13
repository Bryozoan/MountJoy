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

#global pThinSectionData
#global mLabels

#set the figure resolution much higher:
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 500

#import thinsection data from excel 
dFthinSectionData = pd.read_excel(r'C:\Users\therobe7\OneDrive\SRC_and_Research\MountJoy\TimpoweapDataSheet_v3.xlsx',\
                                  sheet_name = 'AllData')

mLabels = pd.read_excel(r'C:\Users\therobe7\OneDrive\SRC_and_Research\MountJoy\TimpoweapDataSheet_v3.xlsx',\
                                  sheet_name = 'Labels')
    

#dFthinSectionData = pd.read_excel(r'C:\Users\duckm\OneDrive\SRC_and_Research\MountJoy\TimpoweapDataSheet_v3.xlsx',\
#                                  sheet_name = 'AllData')

#mLabels = pd.read_excel(r'C:\Users\duckm\OneDrive\SRC_and_Research\MountJoy\TimpoweapDataSheet_v3.xlsx',\
#                                  sheet_name = 'Labels')


dFthinSectionData.set_index('Sample', inplace=True);


#print(dFthinSectionData)

#Normalize the data  (note, this step doesnt need to be done on this [mountjoy] 
#project because all the data is already represented as percent, or already 
#normalized. If you copy this code to use elseware you need to normalize your 
#data)
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
ax.scatter(pThinSectionData[:,0],pThinSectionData[:,1],pThinSectionData[:,2], c=mLabels['MorphColorV2'], marker="o")
#ax.scatter(pThinSectionData[0:8,0],pThinSectionData[0:8,1],pThinSectionData[0:8,2], c="blue", marker="o") # plot the point (2,3,4) on the figure
#ax.scatter(pThinSectionData[9:28:,0],pThinSectionData[9:28,1],pThinSectionData[9:28,2],c="red", marker="x")
plt.show()

#pSumData = pd
#pSumData[:,1] = pThinSectionData.sum(axis=1)

#Set the figure resolution much higher:
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 500

fig = plt.figure(figsize = (25,8))
ax = fig.add_subplot(1,1,1)
#ax.legend(labels=mLabels['Index'])
ax.set_xlabel('Distance', fontsize = 15)
ax.set_ylabel('Principal Component 1', fontsize = 15)
ax.set_title('PCA for Transect', fontsize = 20)

#Plot PCA
ax.scatter(mLabels['x-coord'],pThinSectionData[:,0], c=mLabels['MorphColorV2'], marker="o") 
ax.text(mLabels['x-coord'], pThinSectionData[:,0], mLabels['y-layer'])


plt.show()
