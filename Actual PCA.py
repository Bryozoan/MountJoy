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

#set the figure resolution much higher:
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 500

#import thinsection data from excel 
dFthinSectionData = pd.read_excel(r'C:\Users\therobe7\OneDrive\SRC_and_Research\MountJoy\TimpoweapDataSheet_v3.xlsx',\
                                  sheet_name = 'AllData');
#dFthinSectionData = pd.read_excel(r'C:\Users\duckm\OneDrive\SRC_and_Research\MountJoy\TimpoweapDataSheet_v3.xlsx',\
#                                  sheet_name = 'AllData');

#point where to look
dFthinSectionData.set_index('Sample', inplace=True);

mLabels = pd.read_excel(r'C:\Users\therobe7\OneDrive\SRC_and_Research\MountJoy\TimpoweapDataSheet_v3.xlsx',\
                                  sheet_name = 'Labels')
#mLabels = pd.read_excel(r'C:\Users\duckm\OneDrive\SRC_and_Research\MountJoy\TimpoweapDataSheet_v3.xlsx',\
#                                  sheet_name = 'Labels')


   
#print(dFthinSectionData)

#Normalize the data
#scalerData = StandardScaler(dFthinSectionData);

#Run the PCA
pca = PCA(.70)
pca.fit(dFthinSectionData)
pThinSectionData = pca.transform(dFthinSectionData)
print(pca.n_components_)


fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
ax.legend(labels=mLabels['Index'])
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Component PCA', fontsize = 20)
tPCA = pca.components_
vVar = pca.explained_variance_ratio_
print('Varience accounted by main principal componentes', vVar)

#Plot the 2 PCA
ax.scatter(pThinSectionData[:,0],pThinSectionData[:,1], c=mLabels['MorphColorV2'], marker="o") 

plt.show()


def depthLog(df, indicator, location, depth):
    


    
    locID = df[location].unique()
    dSize = locID.size
    print('Locations:', locID)
    
    listEl = list()
    listDep = list()

    data = {'col':['b','r','g','c','m','blueviolet','teal','palevioletred','gold',\
                      'darkgreen'],'mark':['o','s','^','p','*','d','X','>','<','v']}
    sym = pd.DataFrame(data)
    
    
    for i in range(dSize):
        
        dfNew = df.dropna(subset=[indicator])
        
        listEl.append(dfNew[indicator].where(dfNew[location].eq(locID[i])))
        listDep.append(dfNew[depth].where(dfNew[location].eq(locID[i])))
    
        fig, ax = plt.plot(listEl[i], listDep[i])
        plt.xlabel(indicator) 
        plt.ylabel('Depth ')
        plt.title(indicator + ' at outcrop %f' % locID[i])
        plt.gca().invert_yaxis()
        plt.show()

df = pd.DataFrame(pThinSectionData, columns= ['PCA 1', 'PCA 2', 'PCA 3', 'PCA 4'])     
df['Lateral Sort Order'] = mLabels['Lateral Sort order']
df['Lateral Index'] = mLabels['Lateral Index']
df['Vertical Sort Order'] = mLabels['Vertical Sort Order']
df['Vertical Index'] = mLabels['Vertical Index']


depthLog(df, 'PCA 1', 'Vertical Index', 'Vertical Sort Order')
