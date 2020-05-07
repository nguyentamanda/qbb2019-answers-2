#!/usr/bin/env python3

from __future__ import division #will change / to mean true division, // for floor division
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import numpy.random as rnd

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
    
# print(unfolded_hist)
# print(unfolded_edges)
# print(unfolded_center)

folded_hist, folded_edges = np.histogram(fold, bins = 20)
folded_center = np.mean(np.vstack([folded_edges[0:-1], folded_edges[1:]]), axis = 0)

fig, ax = plt.subplots()

ax.bar(unfolded_center, height = list(unfolded_hist), width = 1, color = "blue", label = "unfolded")
ax.bar(folded_center, height = list(folded_hist), width = 1, color = "red", label = "folded")

ax.legend()
ax.set_xlabel("Waiting time")

fig.savefig("histogram.png")
plt.close(fig)

