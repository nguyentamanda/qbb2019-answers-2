#!/usr/bin/env python3

"""
./03-FreeEnergyII.py

"""
import numpy as np
import matplotlib.pyplot as plt

def FreeEnergy(kcal, tm, t, cp):
    deltaH = kcal * 4.184
    Tm = tm + 273 
    t1 = t 
    Cp = cp * 0.004184
    deltaG = (deltaH)*(1 - (t1/Tm)) + Cp * (t1 * (1- np.log(t1/Tm)) - Tm )
    return deltaG #units are kJ/mol

temp = [] 

dG1 = []
dG2 = []
dG3 = []


for value in range(0,101): 
    value = value + 273
    temp.append(value)

for val in temp:
    t = val
    kcal = 100 #deltaH
    tm = 50
    cp = 0
    case1 = FreeEnergy(kcal, tm, t, 0)
    dG1.append(case1)

for valu in temp:
    t = valu
    kcal = 100
    tm = 50
    cp = 1500
    case1 = FreeEnergy(kcal, tm, t, cp)
    dG2.append(case1)
    
for valu in temp:
    t = valu
    kcal = 100
    tm = 50
    cp = 3000
    case1 = FreeEnergy(kcal, tm, t, cp)
    dG3.append(case1)
    
fig, ax = plt.subplots()

ax.plot(temp, dG1, color = "red", label = "Case 1")
ax.plot(temp, dG2, color = "blue", label = "Case 2")
ax.plot(temp, dG3, color = "green", label = "Case 3")

plt.legend(loc = "upper right")
ax.set_xlabel ("Temperature (K)")
ax.set_ylabel("DeltaG (KJ/mol)")

fig.savefig("3_Free_Energy.png")
plt.close(fig)
