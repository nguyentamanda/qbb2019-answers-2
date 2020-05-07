#!/usr/bin/env python3

"""
./02-Population_Simulation2.py 
"""

import math as mt
import matplotlib.pyplot as plt 

def deltaG(kcal, tm, t):
    deltaH = kcal * 4.184
    Tm = tm + 273 
    t1 = t 
    deltaG = (deltaH)*(1 - (t1/Tm))
    return deltaG #units kJ/mol
    
def StatWeightFolded(dG, t, r):
    k = mt.exp(-dG/(t*r))
    statwgt = 1/(1+k)
    return statwgt

def StatWeightUnfolded(dG, t, r):
    k = mt.exp(-dG/(t*r))
    statwgt = k/(1+k)
    return statwgt

temp = []
for value in range(0,101): 
    value = value + 273
    temp.append(value)

dG1 = []
for val in temp:
    t = val
    kcal = 50
    tm = 50
    case1 = deltaG(kcal, tm, t)
    dG1.append(case1)  

dG2 = []
for val in temp:
    t = val
    kcal = 100
    tm = 50
    case1 = deltaG(kcal, tm, t)
    dG2.append(case1)
    
dG3 = []
for val in temp:
    t = val
    kcal = 150
    tm = 50
    case1 = deltaG(kcal, tm, t)
    dG3.append(case1)
    
r = 0.008314 #kJ/K*mol

statwghtfolded1 = [] 
statwghtunfolded1 = []
for value in range(0,101): 
    val1 = StatWeightFolded(dG1[value], temp[value], r)
    val2 = StatWeightUnfolded(dG1[value], temp[value], r)
    statwghtfolded1.append(val1)
    statwghtunfolded1.append(val2)

statwghtfolded2 = [] 
statwghtunfolded2 = []
for value in range(0,101): 
    val1 = StatWeightFolded(dG2[value], temp[value], r)
    val2 = StatWeightUnfolded(dG2[value], temp[value], r)
    statwghtfolded2.append(val1)
    statwghtunfolded2.append(val2)

statwghtfolded3 = [] 
statwghtunfolded3 = []
for value in range(0,101): 
    val1 = StatWeightFolded(dG3[value], temp[value], r)
    val2 = StatWeightUnfolded(dG3[value], temp[value], r)
    statwghtfolded3.append(val1)
    statwghtunfolded3.append(val2)
    
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)

ax1.plot(temp, statwghtfolded1, color = "red", label = "Folded")
ax1. plot(temp, statwghtunfolded1, color = "blue", label = "Unfolded")
ax1.set_xlabel("Temperature (K)")
ax1.set_ylabel("Probability")
ax1.set_title("Case 1")

ax2.plot(temp, statwghtfolded2, color = "red", label = "Folded")
ax2. plot(temp, statwghtunfolded2, color = "blue", label = "Unfolded")
ax2.set_xlabel("Temperature (K)")
ax2.set_ylabel("Probability")
ax2.set_title("Case 2")

ax3.plot(temp, statwghtfolded3, color = "red", label = "Folded")
ax3. plot(temp, statwghtunfolded3, color = "blue", label = "Unfolded")
ax3.set_xlabel("Temperature (K)")
ax3.set_ylabel("Probability")
ax3.set_title("Case 3")

plt.legend(loc = "upper right")
fig.set_size_inches(10,5)
plt.tight_layout()
fig.savefig("2_Population_Simulations_A.png")
plt.close(fig)

