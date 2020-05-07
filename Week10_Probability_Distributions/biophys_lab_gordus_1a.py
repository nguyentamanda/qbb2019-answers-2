#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Andrew Gordus
April, 2020
Quantitative Biology and Biophysics (AS.020.674/250.644)	Spring 2020
Gordus Lab #1

"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import math

file_path = '/Users/cmdb/qbb2019-answers-2/Week10_Probability_Distributions/'
fname  = 'bob_pairing_data_b.xlsx'
fname = file_path + fname


data_df = pd.read_excel(fname)

#convert dataframe to numpy array
data_n = data_df.to_numpy()
data_n = pd.to_numeric(data_n[:,0])
data_n.resize(18,100)
data_n = np.transpose(data_n)

# Set up the matplotlib figure
f, axes = plt.subplots(2, 2, figsize=(7, 7))
sns.despine(left=True)
sns.set(style="whitegrid")


sns.swarmplot(x=data_df.columns[1], y=data_df.columns[0], data=data_df,ax=axes[0, 0])

sns.violinplot(x=data_df.columns[1], y=data_df.columns[0], data=data_df,ax=axes[0, 1])

sns.boxplot(x=data_df.columns[1], y=data_df.columns[0], data=data_df,ax=axes[1, 0])

sns.barplot(x=data_df.columns[1], y=data_df.columns[0], data=data_df,ax=axes[1, 1])

# plt.show()


# Gaussian
mu = np.nanmean(data_n)
sigma = np.nanstd(data_n)

def gauss_fun(x,mu,sigma):
    exp = np.exp(- (x-mu)**2 / (2*sigma**2))
    denom = np.sqrt(2*3.14*sigma**2)
    p = (1/denom)*exp
    return p
# w = gauss_fun(data_n, mu, sigma)

# Gaussian logL
def gausslogl(x):
    # gauss = gauss_fun(data_n, mu, sigma)
    summ = np.sum(np.log(x))
    return summ 
# print(gausslogl(w))



# Double Gaussian LogL
# NOTE: It returns the NEGATIVE of the logL

def dgausslogl(params,x): 

    mu1 = params[0]
    mu2 = params[1]
    sigma1 = params[2]
    sigma2 = params[3]
    w = params[4]

    if mu1 < np.nanmin(x):
        mu1 = np.nanmin(x)
    elif mu1 > np.nanmax(x):
        mu1 = np.nanmax(x)

    if mu2 < np.nanmin(x):
        mu2 = np.nanmin(x)
    elif mu2 > np.nanmax(x):
        mu2 = np.nanmax(x)
        
    if sigma1 <= 0:
        sigma1 = 0.0001

    if sigma2 <= 0:
        sigma2 = 0.0001

    if w <= 0:
        w = 0.0001
    elif w > 1:
        w = 1 - 0.0001
    #
    # exp1 = np.exp(- (x-mu1)**2 / (2*sigma1**2))
    # denom1 = np.sqrt(2*3.14*sigma1**2)
    # p1 = (w/denom1)*exp1
    #
    # exp2 = np.exp(- (x-mu2)**2 / (2*sigma2**2))
    # denom2 = np.sqrt(2*3.14*sigma2**2)
    # p2 = ((1-w)/denom2)*exp1
    #
    # log = np.log(p1+p2)
    # summ = np.sum(log)
    
    dp = w * np.exp((-(x-mu1)**2) / (2 * sigma1**2)) / (2 * math.pi * sigma1**2)**(1/2) +\
        (1-w) * np.exp((-(x-mu2)**2) / (2 * sigma2**2)) / (2 * math.pi * sigma2**2)**(1/2)
    dlnl = np.sum(np.log(dp))
    return dlnl
    

# Find most probable values for double gaussian
params0 = [mu-sigma,mu+sigma,sigma,sigma,0.6]
result = minimize(dgausslogl, params0, args=data_n, method='Nelder-Mead')

b1 = gauss_fun(data_n, params0[0], params0[2])
b1a = gausslogl(b1)

b2 = gauss_fun(data_n, params0[1], params0[3])
b2a = gausslogl(b2)


# BIC: Best model has LOWEST BIC

k = [2,5]
logL1 = gausslogl(data_n)
logL2 = -dgausslogl(result.x,data_n)

def bic_calc(n,k,logL1,logL2):
    bic1 = k[0]*np.log(n) - 2*np.log(result.x)
    bic2 = k[1]*np.log(n) - 2*np.log(result.x)
    return bic1, bic2


print(-dgausslogl(result.x,data_n))

BIC = bic_calc(100, k, logL1, logL2)
print(BIC[0], BIC[1])
