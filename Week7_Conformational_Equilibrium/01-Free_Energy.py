#!/usr/bin/env python3

"""
./01-equilibrum.py

Plots deltaG
"""
from matplotlib import pyplot as plt
       
def FreeEnergy(kcal, tm, t):
    deltaH = kcal * 4.184
    Tm = tm + 273 
    t1 = t 
    deltaG = (deltaH)*(1 - (t1/Tm))
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
    kcal = 50
    tm = 50
    case1 = FreeEnergy(kcal, tm, t)
    dG1.append(case1)

for valu in temp:
    t = valu
    kcal = 100
    tm = 50
    case1 = FreeEnergy(kcal, tm, t)
    dG2.append(case1)
    
for valu in temp:
    t = valu
    kcal = 150
    tm = 50
    case1 = FreeEnergy(kcal, tm, t)
    dG3.append(case1)

    
fig, ax = plt.subplots()

ax.plot(temp, dG1, color = "red", label = "Case 1")
ax.plot(temp, dG2, color = "blue", label = "Case 2")
ax.plot(temp, dG3, color = "green", label = "Case 3")

plt.legend(loc = "upper right")
ax.set_xlabel ("Temperature (K)")
ax.set_ylabel("DeltaG (KJ/mol)")

fig.savefig("1_Free_Energy.png")
plt.close(fig)

    

