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
from GeochemPlots import hist

#set the figure resolution much higher:
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 500

#import thinsection data from excel 
#dFthinSectionData = pd.read_excel(r'C:\Users\therobe7\OneDrive\SRC_and_Research\MountJoy\TimpoweapDataSheet_v3.xlsx',\
#                                  sheet_name = 'AllData');
dFthinSectionData = pd.read_excel(r'C:\Users\duckm\OneDrive\SRC_and_Research\MountJoy\TimpoweapDataSheet_v3.5.xlsx',\
                                  sheet_name = 'AllData');

#point where to look
dFthinSectionData.set_index('Sample', inplace=True);

#mLabels = pd.read_excel(r'C:\Users\therobe7\OneDrive\SRC_and_Research\MountJoy\TimpoweapDataSheet_v3.xlsx',\
#                                  sheet_name = 'Labels')
mLabels = pd.read_excel(r'C:\Users\duckm\OneDrive\SRC_and_Research\MountJoy\TimpoweapDataSheet_v3.5.xlsx',\
                                  sheet_name = 'Labels')


#set up diferent symbols when making chart
data = {'marker':["o","s","D"]}
sym = pd.DataFrame(data)

#Normalize the data
#scalerData = StandardScaler(dFthinSectionData);
dfNorm = dFthinSectionData.loc[:,"Irregular fenestra":"Seafloor micrite"].divide(dFthinSectionData["Correction factor"], axis="index")
#dfNorm = dFthinSectionData.loc[:,"Fenestra":"cements/encrustations"].divide(dFthinSectionData["Correction factor"], axis="index")
#dFthinSectionData = dFthinSectionData.drop(['Sum','Correction factor'], axis=1)
dFthinSectionData = dFthinSectionData.loc[:,"Irregular fenestra":"Seafloor micrite"]
#dFthinSectionData = dFthinSectionData.loc[:,"Fenestra":"cements/encrustations"]


#Run the PCA on raw data
pca = PCA(.70)
pca.fit(dFthinSectionData)
pThinSectionData = pca.transform(dFthinSectionData)
print(pca.n_components_)

#Run the PCA on normalized data
pcaNorm = PCA(.70)
pcaNorm.fit(dfNorm)
pThinSectionDataNorm = pca.transform(dfNorm)
print(pca.n_components_)


##remove data that we don't know where it is from
#raw Data
pTSD = pd.DataFrame(pThinSectionData, columns = ['PCA1','PCA2','PCA3','PCA4'])
#pTSD = pd.DataFrame(pThinSectionData, columns = ['PCA1','PCA2', 'PCA3'])
pTSD = pTSD.join(mLabels['MorphologyV4'])
pTSD = pTSD.dropna(subset = ['MorphologyV4'])
pTSD = pTSD.drop(columns = ['MorphologyV4'])
#normalized data
pTSDN = pd.DataFrame(pThinSectionDataNorm, columns = ['PCA1','PCA2','PCA3','PCA4'])
#pTSDN = pd.DataFrame(pThinSectionDataNorm, columns = ['PCA1','PCA2', 'PCA3'])
pTSDN = pTSDN.join(mLabels['MorphologyV4'])
pTSDN = pTSDN.dropna(subset = ['MorphologyV4'])
pTSDN = pTSDN.drop(columns = ['MorphologyV4'])
#drop labels we dont have
mLabels = mLabels.dropna(subset = ['MorphologyV4'])

#Plot raw data
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
ax.scatter(pTSD['PCA1'],pTSD['PCA2'], c=mLabels['MorphColorV4'], marker="o") 

plt.show()


#Plot normalized data
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
#ax.legend(labels=pcaNorm())
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('Normalized 2 Component PCA', fontsize = 20)
tPCA = pca.components_
vVar = pca.explained_variance_ratio_
print('Varience accounted by main principal componentes', vVar)

#Plot the 2 PCA
ax.scatter(pTSDN['PCA1'],pTSDN['PCA2'], c=mLabels['MorphColorV4'], marker="o") 

plt.show()


dfHist = pd.concat([pTSDN, mLabels.reindex(pTSDN.index)], axis=1)

hist(dfHist,'PCA1','MorphologyV4','PCA1','labels')
hist(dfHist,'PCA2','MorphologyV4','PCA1','labels')
hist(dfHist,'PCA3','MorphologyV4','PCA1','labels')
hist(dfHist,'PCA4','MorphologyV4','PCA1','labels')



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


#depthLog(df, 'PCA 1', 'Vertical Index', 'Vertical Sort Order')
