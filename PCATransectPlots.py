# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:35:08 2022

@author: duckm
"""

# =============================================================================
# INTRODUCTION:
#
# This code section is to build PCA component graphs for cross section analysis
# 
# For this code you first need to get the component data from "PCA3D.py"\
#     Because you need to get the PCA data we will assume you just ran the\
#     PCA3D modual, and still have the variable loaded. This is called in
#     the code as 'pThinSectionData'
#     
#     The more you know, the more you kohls...
# 
# =============================================================================

 
#Setup 
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Set the figure resolution much higher:
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 500


fig = plt.figure(figsize = (20,8))
ax = fig.add_subplot(1,1,1)
#ax.legend(labels=mLabels['Index'])
ax.set_xlabel('Distance', fontsize = 15)
ax.set_ylabel('Principal Component 1', fontsize = 15)
ax.set_title('PCA1 for Transect', fontsize = 20)


#Plot the 2 PCA
ax.scatter(mLabels['x-coord'],pThinSectionData[:,0], c=mLabels['Color'], marker="o") 


plt.show()