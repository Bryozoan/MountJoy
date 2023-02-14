#-*-coding:utf-8-*-
"""
CreatedonFriFeb1016:46:032023

@author:duckm
"""
#import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import the excel sheet into dataframe
df = pd.read_excel(r'C:\Users\duckm\OneDrive\SRC_and_Research\MountJoy\TimpoweapDataSheet_v4.xlsx'\
                   ,sheet_name='AllData')

#collect subsect of data
sub_df = df.loc[:, 'Irregular fenestra':'Arborescent film and cement']

#create matricies of covariance and correlation
cov = sub_df.cov()
cor = sub_df.corr()

#Create figures
fig = plt.figure(figsize=(33,15))

ax1 = fig.add_subplot(1,2,1)
ax1.set_title('Covariance Matrix')
sns.heatmap(cov,annot=True,cmap='viridis',ax=ax1)

ax2 = fig.add_subplot(1,2,2)
ax2.set_title('Correlation Matrix')
sns.heatmap(cor,annot=True,vmin=-1,vmax=1,cmap='coolwarm',ax=ax2)

fig.tight_layout()
