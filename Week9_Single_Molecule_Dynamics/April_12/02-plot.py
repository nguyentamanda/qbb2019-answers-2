#!/usr/bin/env python3

from __future__ import division #will change / to mean true division, // for floor division
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import numpy.random as rnd
import math as mt 

matplotlib.rcParams.update({"axes.formatter.limits": (-3,3)})
plotStyles={"markersize":10,"markeredgewidth":2.0,"linewidth":2.0}
stepStyles={"markersize":12,"markeredgewidth":3.0,"linewidth":3.0,"where":"post"}


k1=0.15
k2=0.07

ts=[0.0]   # a list of the times when a state change has occurred
states=[0] # state 0 is unfolded, state 1 is folded
tf=1000.0   # the final time of the simulation

while (ts[-1]<tf): 
    
    # If we are in the unfolded state, figure out when the molecule transitions to the folded state.
    if states[-1] == 0:
        ts.append(ts[-1]+rnd.exponential(1/k1))
        states.append(1)
        
    # If we are in the folded state, figure out when the molecule transitions to the unfolded state.
    else:
        ts.append(ts[-1]+rnd.exponential(1/k2))
        states.append(0)

matplotlib.rcParams.update({'font.size': 15, "figure.figsize": (15,5)})
step(ts,states, **stepStyles)
xlabel('t'); ylim([-0.1,1.1]); ylabel('State');

res = [y-x for x, y in zip(ts, ts[1:])]

fold = [res[0:len(res):2]]
unfold = [res[1:len(res):2]]



unfolded_hist, unfolded_edges= np.histogram(unfold, bins = 20)
unfolded_center = np.mean(np.vstack([unfolded_edges[0:-1], unfolded_edges[1:]]), axis = 0)
    
unfolded_sum = sum(unfolded_hist)
unfolded_width = unfolded_edges[1]-unfolded_edges[0]

unfolded_PDF = []

for value in unfolded_hist:
    unfolded_PDF.append(value / (unfolded_sum * unfolded_width))


folded_hist, folded_edges = np.histogram(fold, bins = 20)
folded_center = np.mean(np.vstack([folded_edges[0:-1], folded_edges[1:]]), axis = 0)

folded_sum = sum(folded_hist)
folded_width = folded_edges[1]-folded_edges[0]

folded_PDF = []

for value in folded_hist:
    folded_PDF.append(value / (folded_sum * folded_width))


unfold_eq = []
for t in unfolded_center: 
    ex = mt.exp(-k1*t)
    unfold_eq.append(k1*ex)

fold_eq = []
for t in folded_center: 
    ex = mt.exp(-k2*t)
    fold_eq.append(k2*ex)



fig, ax = plt.subplots(nrows = 1, ncols =2)

ax[0].bar(unfolded_center, height = list(unfolded_PDF), width = 1, color = "blue", label = "unfolded")
ax[1].bar(folded_center, height = list(folded_PDF), width = 1, color = "red", label = "folded")

ax[0].plot(unfolded_center, unfold_eq, color = "black")
ax[1].plot(folded_center, fold_eq, color = "black")

ax[0].legend()
ax[1].legend()
ax[0].set_xlabel("Waiting time")
ax[1].set_xlabel("Waiting time")
ax[0].set_ylabel("Probaility")
ax[1].set_ylabel("Probaility")
#
fig.savefig("PDF.png")
plt.close(fig)





    

 
