# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 10:12:05 2022

@author: therobe7
"""

import pandas as pd
#from sklearn.preprocessing import StandardScaler
#from sklearn.decomposition import PCA
#import plotly to plot PCA
#import matplotlib to plot histograms
import matplotlib.pyplot as plt
from SimpleStats import dfToStat

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


#set up diferent symbols when making chart
data = {'marker':["o","s","D"]}
sym = pd.DataFrame(data)

#Normalize the data
#scalerData = StandardScaler(dFthinSectionData);
dfNorm = dFthinSectionData.loc[:,"Irregular fenestra":"Seafloor micrite"].divide(dFthinSectionData["Correction factor"], axis="index")
dFthinSectionData = dFthinSectionData.drop(['Sum','Correction factor'], axis=1)

dfNorm = dfNorm.reset_index()

dfNorm = dfNorm.join(mLabels['MorphologyV4'])
#dfNorm = dfNorm.dropna(subset = ['MorphologyV4'])

dfCore = dfNorm.where(dfNorm['MorphologyV4'].eq('Core'))
dfCore = dfCore.dropna(subset=['Sample'])
dfPond = dfNorm.where(dfNorm['MorphologyV4'].eq('Pond'))
dfPond = dfPond.dropna(subset=['Sample'])

mean, sd, median, skewness, kertosis, minimum, maximum, variance = dfToStat(dfCore, 'Irregular fenestra', 'Seafloor micrite')

Pmean, Psd, Pmedian, Pskewness, Pkertosis, Pminimum, Pmaximum, Pvariance = dfToStat(dfPond, 'Irregular fenestra', 'Seafloor micrite')

mean = pd.Series(mean)
median = pd.Series(median)
Pmean = pd.Series(Pmean)
Pmedian = pd.Series(Pmedian)
sd = pd.Series(sd)
Psd = pd.Series(Psd)
variance = pd.Series(variance)
Pvariance = pd.Series(Pvariance)




dfT = pd.concat([mean, sd, median, skewness, kertosis, minimum, maximum, variance,\
                 Pmean, Psd, Pmedian, Pskewness, Pkertosis, Pminimum, Pmaximum, Pvariance],\
                axis=1)
    
